# -*- coding: utf-8 -*-
"""
Excel treatment specification parser + Squish comparison helper.

This module DOES NOT navigate the GUI or read Qt objects.
Your recorded Squish script supplies the already-extracted application
values as a Python dictionary. This module finds the exact Excel row and
compares the supplied values with Def/Min/Max.

Requires: openpyxl in the Python interpreter used by Squish.

Example:
    import treatment_excel_compare as excel_check

    excel_check.load_specification(
        r"/path/to/tables parse.xlsx"
    )

    app_values = {
        "frequency":     {"default": 10, "min": 3, "max": 30},
        "pulse_energy":  {"default": 1,  "min": 0.5, "max": 2},
        "average_power": {"default": 10, "min": 3, "max": 20},
        "peak_power":    {"default": 500, "min": 500, "max": 500}
    }

    excel_check.validate_selection(
        family="STONE_ASSISTANT",
        procedure="KIDNEY",
        preset="FRAGMENTATION",
        flow_rate="MEDIUM",
        density="500-1000",
        actual_values=app_values
    )

For Table 1 use family="PRESET_LIST", procedure="STONE" or
"SOFT TISSUE", and the complete Excel preset name.

For Table 2 use family="PROCEDURE_TABLE", procedure="BPH" or
"SOFT TISSUE", and the procedure name from column B.

For the matrix, use family="STONE_ASSISTANT", procedure=organ,
preset=treatment, flow_rate and density.
"""

from __future__ import print_function
import os
import re
import math
import csv
import re
from collections import defaultdict

try:
    import openpyxl
except ImportError:
    openpyxl = None

# ---------------------------- CONFIGURATION ----------------------------

DEFAULT_REPORT = os.path.join(os.getcwd(), "treatment_comparison_log.csv")
ABS_TOLERANCE = 0.0001
REL_TOLERANCE = 0.00001

PARAMETER_COLUMNS_TABLE1 = {
    "frequency":     (4, 5, 6),
    "pulse_energy":  (7, 8, 9),
    "average_power": (10, 11, 12),
    "peak_power":    (13, 14, 15)
}

PARAMETER_COLUMNS_TABLE2 = {
    "frequency":     (3, 4, 5),
    "pulse_energy":  (6, 7, 8),
    "average_power": (9, 10, 11),
    "peak_power":    (12, 13, 14)
}

PARAMETER_COLUMNS_MATRIX = {
    "frequency":     (4, 5, 6),
    "pulse_energy":  (7, 8, 9),
    "average_power": (10, 11, 12),
    "peak_power":    (13, 14, 15)
}

_RECORDS = []
_NA_ROUTES = []
_REPORT_ROWS = []
_SOURCE_FILE = None
_REPORT_FILE = DEFAULT_REPORT


# ---------------------------- NORMALIZATION ----------------------------

def _s(value):
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()
    


def _normalize_preset_name(value):
    """
    Normalizes General Preset names for Excel matching.
    Does not modify existing table normalization.
    """
    if value is None:
        return ""

    value = str(value).strip().upper()

    # Remove spaces around punctuation and normalize separators.
    value = re.sub(r"[-_]+", " ", value)

    # Remove brackets and other punctuation.
    value = re.sub(r"[^\w\s]", " ", value)

    # Collapse multiple spaces.
    value = re.sub(r"\s+", " ", value)

    return value.strip()



def _key(value):
    """Normalize identity text, not numeric parameter values."""
    value = _s(value).upper()
    value = value.replace("\u2264", "<=").replace("\u2265", ">=")
    value = value.replace("HOUNSFIELD SCALE", "")
    value = value.replace("HOUNSFIELD", "")
    value = value.replace("HU", "")
    value = value.replace("(", " ").replace(")", " ")
    value = value.replace("_", " ")
    value = re.sub(r"\s+", " ", value).strip()

    aliases = {
        "LOW FLOW": "LOW",
        "MEDIUM FLOW": "MEDIUM",
        "HIGH FLOW": "HIGH",
        "LOW": "LOW",
        "MEDIUM": "MEDIUM",
        "HIGH": "HIGH",
        "< 500": "<500",
        "<500": "<500",
        "500 1000": "500-1000",
        "500-1000": "500-1000",
        "> 1000": ">1000",
        ">1000": ">1000",
        "N A": "NA",
        "N/A": "NA",
        "NOT APPLICABLE": "NOT APPLICABLE",
        "SOFT TISSUE": "SOFT TISSUE"
    }
    return aliases.get(value, value)


def _value(value):
    """Preserve text tokens such as CW/N/A; convert numeric cells to float."""
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return float(value)
    raw = _s(value)
    if not raw:
        return None
    upper = raw.upper()
    if upper in ("NA", "N/A", "N.A.", "NOT APPLICABLE", "-"):
        return "NA"
    if upper == "CW":
        return "CW"
    try:
        return float(raw.replace(",", ""))
    except Exception:
        return raw


def _same_value(actual, expected):
    if expected is None:
        return actual is None
    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        try:
            return math.isclose(
                float(actual), float(expected),
                rel_tol=REL_TOLERANCE, abs_tol=ABS_TOLERANCE
            )
        except (TypeError, ValueError):
            return False
    return _key(actual) == _key(expected)


# ---------------------------- RECORD BUILDERS ----------------------------

def _blank_parameters():
    return {
        name: {"default": None, "min": None, "max": None}
        for name in ("frequency", "pulse_energy", "average_power", "peak_power")
    }


def _extract_parameters(ws, row, column_map):
    params = _blank_parameters()
    for name, (def_col, min_col, max_col) in column_map.items():
        params[name] = {
            "default": _value(ws.cell(row, def_col).value),
            "min": _value(ws.cell(row, min_col).value),
            "max": _value(ws.cell(row, max_col).value)
        }
    return params

def _get_excel_cell(rec, parameter, field):
    
    _log("DEBUG: _get_excel_cell CALLED")
    family = rec["family"].replace(" ", "_")

    column_maps = {
        "PRESET_LIST": PARAMETER_COLUMNS_TABLE1,
        "PROCEDURE_TABLE": PARAMETER_COLUMNS_TABLE2,
        "STONE_ASSISTANT": PARAMETER_COLUMNS_MATRIX
    }

    column_map = column_maps[family]

    field_index = {
        "default": 0,
        "min": 1,
        "max": 2
    }

    column_number = column_map[parameter][field_index[field]]

    column_letter = openpyxl.utils.get_column_letter(column_number)

    return "{}{}".format(column_letter, rec["excel_row"])


def _has_parameter_content(ws, row, column_map):
    for cols in column_map.values():
        for col in cols:
            if ws.cell(row, col).value is not None:
                return True
    return False


def _make_record(family, procedure, preset, row, parameters,
                 flow="", density="", fiber=""):
                 
    family_key = _key(family)

    if family_key == "PRESET LIST":
        preset_key = _normalize_preset_name(preset)
    else:
        preset_key = _key(preset)
        
    return {
        "family": _key(family),
        "procedure": _key(procedure),
        "preset": _key(preset),
        "flow_rate": _key(flow) if flow else "",
        "density": _key(density) if density else "",
        "excel_row": row,
        "fiber": _s(fiber),
        "parameters": parameters
    }


# ---------------------------- TABLE 1 PARSER ----------------------------

def _parse_table1(ws):
    """
    Table 1 signature:
      Row 3: Category / Preset Name / Frequency / Pulse Energy /
             Average Power / Peak Power
      Row 4: Def / Min / Max
      Data: rows with preset name in C; category inherited from B.
    """
    records = []
    header_found = False
    category = ""

    for row in range(1, ws.max_row + 1):
        b = _key(ws.cell(row, 2).value)
        c = _key(ws.cell(row, 3).value)

        if (b == "CATEGORY" and c == "PRESET NAME" and
                _key(ws.cell(row, 4).value) == "FREQUENCY"):
            header_found = True
            continue

        if not header_found:
            continue

        # A new category in column B applies to this and following preset rows.
        if b in ("STONE", "SOFT TISSUE"):
            category = b

        preset_name = _s(ws.cell(row, 3).value)
        if not preset_name:
            continue

        # Stop at the next table heading, rather than assuming a fixed end row.
        if _key(preset_name) in ("PROCEDURE NAME", "FREQUENCY"):
            break

        if not category or not _has_parameter_content(
                ws, row, PARAMETER_COLUMNS_TABLE1):
            continue

        params = _extract_parameters(
            ws, row, PARAMETER_COLUMNS_TABLE1
        )
        records.append(_make_record(
            "PRESET_LIST", category, preset_name, row, params
        ))

    return records


# ---------------------------- TABLE 2 PARSER ----------------------------

def _parse_table2(ws):
    """
    Table 2 signature:
      Section label in B (BPH or Soft Tissue)
      Header row: Procedure Name / Frequency / Pulse Energy /
                  Average Power / Peak Power / Fiber
      Next row: Def/Min/Max subheaders
      Data rows: procedure name in B.
    """
    records = []
    section = ""
    row = 1

    while row <= ws.max_row:
        label = _key(ws.cell(row, 2).value)

        if label in ("BPH", "SOFT TISSUE"):
            section = label
            row += 1
            continue

        is_header = (
            label == "PROCEDURE NAME" and
            _key(ws.cell(row, 3).value) == "FREQUENCY" and
            _key(ws.cell(row, 6).value) == "PULSE ENERGY" and
            _key(ws.cell(row, 9).value) == "AVERAGE POWER" and
            _key(ws.cell(row, 12).value) == "PEAK POWER"
        )

        if is_header and section:
            data_row = row + 2
            while data_row <= ws.max_row:
                procedure_name = _s(ws.cell(data_row, 2).value)
                if not procedure_name:
                    break
                # A new section/header ends this table's data.
                if _key(procedure_name) in ("BPH", "SOFT TISSUE", "PROCEDURE NAME"):
                    break
                if not _has_parameter_content(
                        ws, data_row, PARAMETER_COLUMNS_TABLE2):
                    data_row += 1
                    continue

                params = _extract_parameters(
                    ws, data_row, PARAMETER_COLUMNS_TABLE2
                )
                records.append(_make_record(
                    "PROCEDURE_TABLE", section, procedure_name,
                    data_row, params, fiber=ws.cell(data_row, 15).value
                ))
                data_row += 1

            row = data_row
            continue

        row += 1

    return records


# ---------------------------- TABLE 3 PARSER ----------------------------

def _parse_table3(ws):
    """
    Matrix route:
      Procedure: <treatment> / <organ>
      Flow section in B
      Density data rows have density in C and parameter values in D:O.
      A flow section marked NOT APPLICABLE is retained as an NA route.
    """
    records = []
    na_routes = []
    current_preset = ""
    current_organ = ""
    current_flow = ""

    procedure_re = re.compile(
        r"(?i)^PROCEDURE\s*:\s*(.*?)\s*/\s*(.*?)\s*$"
    )

    for row in range(1, ws.max_row + 1):
        b_raw = _s(ws.cell(row, 2).value)
        b_key = _key(b_raw)
        c_raw = _s(ws.cell(row, 3).value)
        c_key = _key(c_raw)

        match = procedure_re.match(b_raw)
        if match:
            current_preset = _key(match.group(1))
            current_organ = _key(match.group(2))
            current_flow = ""
            continue

        if not current_preset:
            continue

        if b_key in ("LOW", "MEDIUM", "HIGH", "UNKNOWN"):
            current_flow = _key(b_raw)
            continue

        if b_key == "NOT APPLICABLE":
            na_routes.append({
                "family": "STONE_ASSISTANT",
                "procedure": current_organ,
                "preset": current_preset,
                "flow_rate": current_flow,
                "excel_row": row,
                "status": "NOT APPLICABLE"
            })
            continue

        if c_key in ("<500", "500-1000", ">1000", "UNKNOWN"):
            if not current_flow:
                raise ValueError(
                    "Density row %d has no preceding flow-rate section." % row
                )

            params = _extract_parameters(
                ws, row, PARAMETER_COLUMNS_MATRIX
            )
            records.append(_make_record(
                "STONE_ASSISTANT",
                current_organ,
                current_preset,
                row,
                params,
                flow=current_flow,
                density=c_raw,
                fiber=ws.cell(row, 16).value
            ))

    return records, na_routes


# ---------------------------- PUBLIC LOADER / AUDIT ----------------------------

def load_specification(workbook_path, report_path=None):
    """Parse all tables and load records for subsequent validation."""
    global _RECORDS, _NA_ROUTES, _SOURCE_FILE, _REPORT_FILE

    if openpyxl is None:
        raise RuntimeError(
            "openpyxl is unavailable in the Squish Python interpreter."
        )
    if not os.path.isfile(workbook_path):
        raise IOError("Workbook does not exist: " + str(workbook_path))

    wb = openpyxl.load_workbook(workbook_path, data_only=True, read_only=False)
    try:
        if "Sheet1" not in wb.sheetnames:
            raise ValueError("Expected worksheet 'Sheet1' was not found.")
        ws = wb["Sheet1"]

        t1 = _parse_table1(ws)
        t2 = _parse_table2(ws)
        t3, na = _parse_table3(ws)

        records = t1 + t2 + t3

        # Exact duplicate identity keys are an error; never silently choose one.
        index = defaultdict(list)
        for rec in records:
            key = _record_key(
                rec["family"], rec["procedure"], rec["preset"],
                rec["flow_rate"], rec["density"]
            )
            index[key].append(rec["excel_row"])

        duplicates = dict((k, v) for k, v in index.items() if len(v) > 1)
        if duplicates:
            raise ValueError(
                "Duplicate Excel routing keys found: %s" % duplicates
            )

        _RECORDS = records
        _NA_ROUTES = na
        _SOURCE_FILE = os.path.abspath(workbook_path)
        if report_path:
            _REPORT_FILE = os.path.abspath(report_path)

        _log("EXCEL LOAD OK | file=%s | sheet=%s" % (_SOURCE_FILE, ws.title))
        _log("TABLE 1 | general preset records=%d" % len(t1))
        _log("TABLE 2 | BPH + Soft Tissue records=%d" % len(t2))
        _log("TABLE 3 | stone matrix records=%d" % len(t3))
        _log("MATRIX N/A ROUTES=%d" % len(na))
        _log("TOTAL APPLICABLE RECORDS=%d" % len(records))
        _log("TOTAL MATRIX ROUTES INCLUDING N/A=%d" % (len(t3) + len(na)))

        return {
            "table1": len(t1),
            "table2": len(t2),
            "table3": len(t3),
            "matrix_na": len(na),
            "total_records": len(records)
        }
    finally:
        wb.close()


def _record_key(family, procedure, preset, flow="", density=""):
    
    family_key = _key(family)
    
    if family_key == "PRESET LIST":
        preset_key = _normalize_preset_name(preset)
    else:
        preset_key = _key(preset)
        
    return (
        family_key,
        _key(procedure),
        preset_key,
        _key(flow) if flow else "",
        _key(density) if density else ""
    )


def find_expected(family, procedure, preset, flow_rate=None, density=None):
    if not _RECORDS:
        raise RuntimeError("Call load_specification() before validation.")

    wanted = _record_key(family, procedure, preset, flow_rate, density)
    matches = []
    for rec in _RECORDS:
        candidate = _record_key(
            rec["family"], rec["procedure"], rec["preset"],
            rec["flow_rate"], rec["density"]
        )
        if candidate == wanted:
            matches.append(rec)

    if not matches:
        na_match = [
            route for route in _NA_ROUTES
            if _record_key(
                route["family"], route["procedure"], route["preset"],
                route["flow_rate"], ""
            ) == _record_key(
                family, procedure, preset, flow_rate, ""
            )
        ]
        if na_match:
            raise LookupError(
                "Selected route is marked NOT APPLICABLE in Excel "
                "(source row %s)." % na_match[0]["excel_row"]
            )
        raise LookupError(
            "No exact Excel record found for route %s" % (wanted,)
        )

    if len(matches) != 1:
        raise LookupError(
            "Ambiguous Excel route %s; matching rows=%s" %
            (wanted, [r["excel_row"] for r in matches])
        )
    return matches[0]


# ---------------------------- SQUISH LOGGING ----------------------------

def _log(message):
    message = str(message)
    try:
        test.log(message)
    except Exception:
        print(message)


def _warning(message):
    message = str(message)
    try:
        test.warning(message)
    except Exception:
        print("WARNING: " + message)

def _write_report():

    if not _REPORT_ROWS:
        _log("CSV REPORT NOT GENERATED: No validation records collected.")
        return

    folder = os.path.dirname(_REPORT_FILE)

    if folder and not os.path.isdir(folder):
        os.makedirs(folder)

    columns = [
        "family", "procedure", "preset", "flow_rate", "density",
        "excel_row", "excel_cell", "parameter", "field",
        "expected", "actual", "result", "detail"
    ]

    with open(_REPORT_FILE, "w", newline="") as handle:

        writer = csv.DictWriter(
            handle,
            fieldnames=columns,
            extrasaction="ignore"
        )

        writer.writeheader()
        writer.writerows(_REPORT_ROWS)

    _log("CSV REPORT GENERATED SUCCESSFULLY")
    _log("CSV LOCATION: {}".format(_REPORT_FILE))
    _log("TOTAL VALIDATION RECORDS: {}".format(len(_REPORT_ROWS)))


# ---------------------------- VALIDATION ----------------------------

def validate_selection(family, procedure, preset, actual_values,
                       flow_rate=None, density=None,
                       fail_test_on_mismatch=False):
    """
    Compare caller-supplied application variables with the exact Excel row.

    actual_values format:
      {
        "frequency":     {"default": ..., "min": ..., "max": ...},
        "pulse_energy":  {"default": ..., "min": ..., "max": ...},
        "average_power": {"default": ..., "min": ..., "max": ...},
        "peak_power":    {"default": ..., "min": ..., "max": ...}
      }

    Values may be numeric or strings. Text tokens such as "CW" and "N/A"
    are supported. A missing actual field is NOT_READ, not PASS.
    """
    rec = find_expected(
        family, procedure, preset, flow_rate, density
    )

    route = {
        "family": _key(family),
        "procedure": _key(procedure),
        "preset": _key(preset),
        "flow_rate": _key(flow_rate) if flow_rate else "",
        "density": _key(density) if density else ""
    }

    _log("=" * 72)
    _log("VALIDATING | %s" % route)
    _log("EXCEL SOURCE | Sheet1 row %s" % rec["excel_row"])

    results = []
    for parameter in (
        "frequency", "pulse_energy", "average_power", "peak_power"
    ):
        expected_group = rec["parameters"][parameter]
        supplied_group = actual_values.get(parameter, {})
        
        for field in ("default", "min", "max"):
            expected = expected_group.get(field)
            actual_present = field in supplied_group
            actual = supplied_group.get(field) if actual_present else None
            
            _log("DEBUG: About to calculate Excel cell")
            excel_cell = _get_excel_cell(rec, parameter, field)
        
            if not actual_present:
                result = "NOT_READ"
                detail = "Application variable was not supplied"
        
            elif expected is None:
                result = "NOT_SPECIFIED"
                detail = "Excel cell is blank"
        
            elif not _same_value(actual, expected):
                result = "FAIL"
                detail = "Expected {}; received {}".format(expected, actual)
        
            else:
                result = "PASS"
                detail = "Matched"
        
            line = {
                "family": route["family"],
                "procedure": route["procedure"],
                "preset": route["preset"],
                "flow_rate": route["flow_rate"],
                "density": route["density"],
                "excel_row": rec["excel_row"],
                "excel_cell": excel_cell,
                "parameter": parameter,
                "field": field,
                "expected": expected,
                "actual": actual,
                "result": result,
                "detail": detail
            }
        
            results.append(result)
            _REPORT_ROWS.append(line)
        
            _log(
                "{} | {} | Excel Cell: {} | Excel Value: {} | "
                "GUI Value: {} | {} | {}".format(
                    parameter,
                    field,
                    excel_cell,
                    expected,
                    actual,
                    result,
                    detail
                )
            )

    failures = results.count("FAIL")
    unread = results.count("NOT_READ")
    passed = results.count("PASS")
    not_specified = results.count("NOT_SPECIFIED")

    _log("SUMMARY | PASS=%d FAIL=%d NOT_READ=%d NOT_SPECIFIED=%d" %
         (passed, failures, unread, not_specified))

    if failures:
        message = "VALIDATION FAILED for %s: %d mismatch(es)." % (
            preset, failures
        )
        _warning(message)
        if fail_test_on_mismatch:
            try:
                test.fail(message)
            except Exception:
                pass
    elif unread or not_specified:
        _warning(
            "VALIDATION INCOMPLETE for {}: NOT_READ={}, NOT_SPECIFIED={}".format(
                preset,
                unread,
                not_specified
            )
        )
    else:
        _log("VALIDATION PASSED for %s" % preset)

    _write_report()
    return {
        "passed": passed,
        "failed": failures,
        "not_read": unread,
        "not_specified": not_specified,
        "excel_row": rec["excel_row"],
        "success": (
            failures == 0
            and unread == 0
            and not_specified == 0
        )
    }


def print_record_index():
    """Write all parsed route keys and source rows to the Squish log."""
    if not _RECORDS:
        raise RuntimeError("Call load_specification() first.")

    for rec in _RECORDS:
        _log(
            "INDEX | row=%s | family=%s | procedure=%s | preset=%s | "
            "flow=%s | density=%s | fiber=%s" %
            (rec["excel_row"], rec["family"], rec["procedure"],
             rec["preset"], rec["flow_rate"], rec["density"], rec["fiber"])
        )


def clear_execution_report():
    global _REPORT_ROWS
    _REPORT_ROWS = []
    if os.path.exists(_REPORT_FILE):
        os.remove(_REPORT_FILE)
