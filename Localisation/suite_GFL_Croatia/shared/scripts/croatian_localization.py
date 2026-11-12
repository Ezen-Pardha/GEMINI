"""Croatian reference data and text checks shared by the Squish cases.

Keep expected translations in the supplied workbook, never in captured UI text.
This module is also importable without Squish for catalogue regression tests.
"""

import html
import os
import re
import unicodedata

from openpyxl import load_workbook


EXCEL_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "testdata", "Gemini Split strings.xlsx"
))
_CACHE = {}


class ReferenceError(ValueError):
    """Missing or ambiguous expected data; do not substitute an observed value."""


def normalize(value):
    if value is None:
        return ""
    text = html.unescape(str(value))
    text = re.sub(r"<br\s*/?>|</(?:p|div)\s*>", " ", text, flags=re.I)
    text = re.sub(r"</?[a-zA-Z][^>]*>", "", text)
    text = unicodedata.normalize("NFC", text).replace("\u200b", "")
    text = text.replace("\\n", " ").replace("μ", "µ")
    # Recorded preset captions insert a separator before parenthesized qualifiers.
    text = re.sub(r"\s*-\s*(?=\()", "", text)
    return " ".join(text.split()).strip().casefold().replace("μ", "µ")


def comparison_key(value):
    # Qt can wrap a word across lines (e.g. AŽURIRA\nJ). Preserve its letters.
    return re.sub(r"\s+", "", normalize(value)).replace("™", "").replace("®", "")


def catalog_rows(sheet_name="GUI Strings", path=None):
    """Read explicit worksheets and locate languages by their column headers.

    reset_dimensions avoids iterating 1,048,576 rows of Excel formatting in
    Treatment Modes/Keyboard. The actual populated XML rows are still read.
    """
    path = os.path.abspath(path or EXCEL_PATH)
    stamp = (path, os.stat(path).st_mtime_ns, os.stat(path).st_size, sheet_name)
    if stamp in _CACHE:
        return [dict(row) for row in _CACHE[stamp]]
    workbook = load_workbook(path, read_only=True, data_only=True)
    try:
        if sheet_name not in workbook.sheetnames:
            raise ReferenceError("Worksheet {!r} not found in {}. Available: {}".format(
                sheet_name, path, ", ".join(workbook.sheetnames)))
        sheet = workbook[sheet_name]
        sheet.reset_dimensions()
        iterator = sheet.iter_rows(values_only=True)
        header = next(iterator, ())
        columns = {normalize(value): index for index, value in enumerate(header) if value}
        if "english" not in columns or "croatian" not in columns:
            raise ReferenceError("English/Croatian column headers missing in {} / {}".format(path, sheet_name))
        english_col, croatian_col = columns["english"], columns["croatian"]
        result = []
        for row_number, row in enumerate(iterator, 2):
            if len(row) <= max(english_col, croatian_col):
                continue
            english, croatian = row[english_col], row[croatian_col]
            if not normalize(english):
                continue
            result.append({
                "english": str(english).strip(),
                "croatian": str(croatian).strip() if croatian is not None else "",
                "trace_id": str(row[0] or "").strip() if english_col != 0 else "",
                "row": row_number, "sheet": sheet_name,
                "normalized": normalize(croatian),
            })
        if not any(row["normalized"] for row in result):
            raise ReferenceError("No Croatian translations in {} / {}".format(path, sheet_name))
        _CACHE[stamp] = result
        return [dict(row) for row in result]
    finally:
        workbook.close()


def translated_rows(sheet_name="GUI Strings"):
    return [row for row in catalog_rows(sheet_name) if row["normalized"]]


def expected_text(english, sheet_name="GUI Strings", trace_id=None):
    """Resolve a key in its context; never silently overwrite LOW/MEDIUM."""
    candidates = [row for row in catalog_rows(sheet_name)
                  if comparison_key(row["english"]) == comparison_key(english)]
    if trace_id:
        candidates = [row for row in candidates
                      if trace_id in {part.strip() for part in row["trace_id"].split(",")}]
    values = {row["croatian"] for row in candidates if row["normalized"]}
    normalized_values = {comparison_key(value) for value in values}
    if not normalized_values:
        raise ReferenceError("No Croatian reference for English {!r} in {!r} (trace {!r})".format(
            english, sheet_name, trace_id))
    if len(normalized_values) != 1:
        raise ReferenceError("Ambiguous English key {!r} in {!r}: {}. Specify its trace context.".format(
            english, sheet_name, sorted(values)))
    return sorted(values)[0]


def is_measurement(text):
    """Only language-neutral numeric values; localized labels are never ignored."""
    return bool(re.fullmatch(
        r"[+-]?\d+(?:[.,]\d+)?(?:/\d+)?(?:%|(?:w|j|kj|hz|µm|ml/min))?"
        r"|\d+min\d+s|\d{1,2}:\d{2}(?::\d{2})?"
        r"|\d{1,4}[-./]\d{1,2}[-./]\d{1,4}", comparison_key(text)))


def _template_match(actual, expected):
    # The approved catalogue uses X/X and X s for numeric placeholders.
    expected = comparison_key(expected)
    if "x/x" in expected:
        pattern = re.escape(expected).replace("x/x", r"\d+/\d+")
        return re.fullmatch(pattern, actual) is not None
    if "xs" in expected and "vrijeme" in expected:
        pattern = re.escape(expected).replace("xs", r"\d+s")
        return re.fullmatch(pattern, actual) is not None
    return False


def match_text(actual, rows=None):
    """Require a complete translation/template, not an arbitrary substring."""
    key = comparison_key(actual)
    rows = translated_rows() if rows is None else rows
    for row in rows:
        if key == comparison_key(row["croatian"]) or _template_match(key, row["croatian"]):
            return row
    # A composite profile label can expose both strings as one Qt text property.
    profile = comparison_key(expected_text("PROFILE:", "Home Screen"))
    if key.startswith(profile):
        tail = key[len(profile):]
        for row in rows:
            if tail and tail == comparison_key(row["croatian"]):
                return row
    return None


def collect_texts(root, children):
    """Read visible widget text; object reprs and hidden pages are not labels."""
    values, visited = [], set()

    def visit(obj, depth=0):
        if obj is None or depth > 40 or id(obj) in visited:
            return
        visited.add(id(obj))
        try:
            if not obj.visible:
                return
        except AttributeError:
            pass
        for attr in ("text", "title", "placeholderText"):
            try:
                value = getattr(obj, attr)
                value = value() if callable(value) else value
                if normalize(value):
                    values.append(str(value))
            except (AttributeError, LookupError, TypeError):
                pass
        try:
            descendants = children(obj)
        except (LookupError, TypeError):
            descendants = []
        for child in descendants:
            visit(child, depth + 1)

    visit(root)
    return list(dict.fromkeys(values))


def verify_texts(texts, screen_name, reporter, rows=None):
    rows = translated_rows() if rows is None else rows
    matched, missing = 0, 0
    for key, actual in {comparison_key(text): text for text in texts if normalize(text)}.items():
        if is_measurement(actual):
            continue
        row = match_text(actual, rows)
        if row:
            reporter.passes("{} | {} -> {}".format(screen_name, row["english"], row["croatian"]))
            matched += 1
        else:
            reporter.fail("{} | No approved Croatian reference matches visible text: {!r}".format(screen_name, actual))
            missing += 1
    if not matched:
        reporter.fail("{} | No translated UI labels were verified".format(screen_name))
    reporter.log("{} | Matched: {} | Unmatched: {}".format(screen_name, matched, missing))
    return bool(matched) and not missing


def verify_screen(root, screen_name, runtime):
    return verify_texts(collect_texts(root, runtime["object"].children), screen_name, runtime["test"])


def verify_object(reference, english, description, runtime, sheet_name="GUI Strings", trace_id=None):
    try:
        expected = expected_text(english, sheet_name, trace_id)
    except ReferenceError as error:
        runtime["test"].fail("{} | REFERENCE DATA: {}".format(description, error))
        return False
    obj = runtime["waitForObject"](reference, 10000)
    return runtime["test"].compare(comparison_key(obj.text), comparison_key(expected),
        "{} | English: {} | Expected Croatian: {}".format(description, english, expected))


def select_croatian(runtime):
    """Establish the locale even when a case runs independently."""
    names = runtime["names"]
    click, wait = runtime["clickButton"], runtime["waitForObject"]
    click(wait(names.homeScreen_settingsButton_QPushButton))
    runtime["clickTab"](wait(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    click(wait(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    click(wait(names.languagesFrame_pbCroatia_QPushButton))
    click(wait(names.buttonsFrame_acceptButton_QPushButton))
    click(wait(names.settingsScreen_pbBack_QPushButton))
    wait(names.homeScreen_HomeScreen)


def click_first_log_row(view, runtime):
    """Localization does not require the third event to exist."""
    model = view.model()
    if model.rowCount() == 0 or model.columnCount() == 0:
        runtime["test"].log("Event log is empty; row interaction is not applicable. Labels are still verified.")
        return False
    column = min(1, model.columnCount() - 1)
    index = model.index(0, column)
    view.scrollTo(index)
    rect = view.visualRect(index)
    runtime["mouseClick"](view, rect.x() + rect.width() // 2,
        rect.y() + rect.height() // 2, runtime["Qt"].NoModifier, runtime["Qt"].LeftButton)
    return True
