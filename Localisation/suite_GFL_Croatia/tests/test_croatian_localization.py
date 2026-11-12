"""Run without an AUT: python3 -m unittest discover -s tests -v."""

import ast
import importlib.util
import json
from pathlib import Path
import runpy
import sys
import tempfile
import types
import unittest

from openpyxl import Workbook

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared/scripts"))
import croatian_localization as loc


class Reporter:
    def __init__(self):
        self.passed, self.failed, self.messages = [], [], []

    def passes(self, message):
        self.passed.append(message)

    def fail(self, message):
        self.failed.append(message)

    def log(self, message):
        self.messages.append(message)


class CatalogTests(unittest.TestCase):
    def test_reads_complete_master_instead_of_saved_active_sheet(self):
        self.assertEqual(loc.expected_text("PROFILE:"), "PROFIL:")
        self.assertEqual(loc.expected_text("ADD PRESET"), "DODAJ ZADANU POSTAVKU")
        self.assertEqual(loc.expected_text("FREQUENCY"), "FREKVENCIJA")

    def test_duplicate_english_keys_require_context(self):
        with self.assertRaisesRegex(loc.ReferenceError, "Ambiguous"):
            loc.expected_text("LOW")
        self.assertEqual(loc.expected_text("LOW", trace_id="TB"), "MALA")
        self.assertEqual(loc.expected_text("LOW", trace_id="TM"), "Slaba")

    def test_uses_popup_title_key_instead_of_button_caption(self):
        self.assertEqual(loc.expected_text("SELECT PEAK POWER", "Treatment Modes"), "ODABIR VRŠNE SNAGE")
        self.assertEqual(loc.expected_text("PEAK POWER", "Treatment Modes"), "VRŠNA SNAGA")

    def test_missing_reference_is_not_an_empty_expected_string(self):
        for english in ("CONFIRM", "Soft Tissue Characteristics", "invented caption"):
            with self.subTest(english=english), self.assertRaises(loc.ReferenceError):
                loc.expected_text(english)

    def test_header_detection_supports_both_workbook_formats(self):
        # Original un-split files put Croatian in I; the shared file uses D.
        with tempfile.TemporaryDirectory() as directory:
            for column in (4, 9):
                workbook = Workbook()
                sheet = workbook.active
                sheet.title = "Reference"
                sheet.cell(1, 2, "English")
                sheet.cell(1, column, "Croatian")
                sheet.cell(2, 2, "SAVE")
                sheet.cell(2, column, "SPREMI")
                path = Path(directory) / (str(column) + ".xlsx")
                workbook.save(path)
                workbook.close()
                self.assertEqual(loc.catalog_rows("Reference", str(path))[0]["croatian"], "SPREMI")

    def test_named_sections_exist_and_all_have_croatian_data(self):
        for name in ("GUI Strings", "Stone", "Soft tissue", "Home Screen", "Treatment Modes"):
            with self.subTest(sheet=name):
                self.assertGreater(len(loc.translated_rows(name)), 0)

    def test_word_wrap_html_and_micro_units_preserve_meaning(self):
        self.assertEqual(loc.comparison_key("PROSJEČNA\nSNAGA"), loc.comparison_key("PROSJEČNA SNAGA"))
        self.assertIsNotNone(loc.match_text("AŽURIRA\nJ"))
        self.assertIsNotNone(loc.match_text('<html><body><p><img src="icon.png"/>UREDI ZADANU POSTAVKU</p></body></html>'))
        self.assertIsNotNone(loc.match_text("stranica 1/3"))
        self.assertIsNotNone(loc.match_text("PROFIL: Zadano"))
        self.assertEqual(loc.comparison_key("200 μm"), loc.comparison_key("200 µm"))

    def test_only_numeric_values_are_exempt_from_localization(self):
        for value in ("10", "12%", "0 J", "0 min 0 s", "200 μm", "10/10"):
            with self.subTest(value=value):
                self.assertTrue(loc.is_measurement(value))
        for value in ("ENGLISH TEXT", "ENERGY 10 J", "BROJ PREOSTALIH UPORABA:"):
            with self.subTest(value=value):
                self.assertFalse(loc.is_measurement(value))

    def test_negative_translation_and_substring_cases_still_fail(self):
        self.assertIsNone(loc.match_text("INCISION"))
        self.assertIsNone(loc.match_text("PROSJEČNA SNAGA UNAPPROVED SUFFIX"))
        self.assertNotEqual(loc.comparison_key("Srednji"), loc.comparison_key("Srednja"))
        self.assertNotEqual(loc.comparison_key("REZ"), loc.comparison_key("REŽ"))

    def test_reference_missing_does_not_pass_even_for_empty_ui_text(self):
        reporter = Reporter()
        result = loc.verify_object({}, "CONFIRM", "Confirm", {"test": reporter})
        self.assertFalse(result)
        self.assertEqual(len(reporter.passed), 0)
        self.assertIn("REFERENCE DATA", reporter.failed[0])

    def test_screen_check_fails_unknown_labels_and_zero_match(self):
        reporter = Reporter()
        self.assertFalse(loc.verify_texts(["FREKVENCIJA", "INCISION"], "Test", reporter))
        self.assertEqual(len(reporter.passed), 1)
        self.assertEqual(len(reporter.failed), 1)
        reporter = Reporter()
        self.assertFalse(loc.verify_texts(["10", "200 μm"], "Empty labels", reporter))
        self.assertTrue(reporter.failed)

    def test_collects_visible_labels_without_object_repr_or_hidden_pages(self):
        root = types.SimpleNamespace(visible=True, text="FREKVENCIJA")
        hidden = types.SimpleNamespace(visible=False, text="HIDDEN ENGLISH")
        child = types.SimpleNamespace(visible=True, text="ENERGIJA IMPULSA")
        values = loc.collect_texts(root, lambda obj: [hidden, child] if obj is root else [])
        self.assertEqual(values, ["FREKVENCIJA", "ENERGIJA IMPULSA"])


class SuiteRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old_helper = sys.modules.get("objectmaphelper")
        # Object map is declarative; this stub permits loading it without Squish.
        sys.modules["objectmaphelper"] = types.ModuleType("objectmaphelper")
        cls.cases = {path.parent.name: runpy.run_path(str(path)) for path in ROOT.glob("tst_*/test.py")}

    @classmethod
    def tearDownClass(cls):
        if cls.old_helper is None:
            sys.modules.pop("objectmaphelper", None)
        else:
            sys.modules["objectmaphelper"] = cls.old_helper

    def test_all_case_catalogue_paths_resolve_inside_this_suite(self):
        for name, values in self.cases.items():
            if "EXCEL_PATH" in values:
                with self.subTest(case=name):
                    self.assertEqual(values["EXCEL_PATH"], loc.EXCEL_PATH)
                    self.assertTrue(Path(values["EXCEL_PATH"]).is_file())

    def test_every_case_loader_returns_correct_croatian_text(self):
        for name, values in self.cases.items():
            if "load_croatian_strings" in values:
                with self.subTest(case=name):
                    rows = values["load_croatian_strings"]()
                    self.assertTrue(rows)
                    self.assertTrue(any(row["english"] == "PROFILE:" and row["croatian"] == "PROFIL:" for row in rows))

    def test_ready_lookup_uses_current_preset_and_pulse_names(self):
        values = self.cases["tst_GEM-LOC-CROATIA-Ready Screen"]
        workbook, data = values["load_excel_data"]()
        try:
            normalize = values["normalize_text"]
            self.assertEqual(data[normalize("PROSTATE ENUCLEATE (HIGH ENERGY)")], "ENUKLEACIJA PROSTATE (VELIKA ENERGIJA)")
            self.assertEqual(data[normalize("REGULAR PULSE")], "STANDARDNI IMPULS")
        finally:
            workbook.close()

    def test_map_aliases_do_not_target_preset_popup(self):
        names = self.cases["tst_LoginScreen"]["names"]
        for symbol in ("croatiaTreatment_averagePowerName_QLabel", "croatiaTreatment_averagePowerUnits_QLabel"):
            selector = getattr(names, symbol)
            while "container" in selector:
                self.assertNotEqual(selector.get("name"), "centralWidget")
                selector = selector["container"]
        self.assertEqual(names.fiberUsesFrame_nameLabel_QLabel["container"]["name"], "fiberUsesFrame")

    def test_all_python_and_active_verification_point_references(self):
        names = self.cases["tst_LoginScreen"]["names"]
        for path in ROOT.rglob("*.py"):
            tree = ast.parse(path.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "names":
                    self.assertTrue(hasattr(names, node.attr), (path, node.lineno, node.attr))
                if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                        and isinstance(node.func.value, ast.Name) and node.func.value.id == "test"
                        and node.func.attr == "vp" and node.args and isinstance(node.args[0], ast.Str)):
                    self.assertTrue((path.parent / "verificationPoints" / node.args[0].s).is_file(), (path, node.args[0].s))

    def test_empty_log_does_not_attempt_a_row_click(self):
        reporter = Reporter()
        model = types.SimpleNamespace(rowCount=lambda: 0, columnCount=lambda: 4)
        view = types.SimpleNamespace(model=lambda: model)
        self.assertFalse(loc.click_first_log_row(view, {"test": reporter}))
        self.assertIn("empty", reporter.messages[0])

    def test_single_log_row_is_selected_without_requesting_row_two(self):
        indices, clicks = [], []
        def index(row, col):
            self.assertEqual(row, 0)
            indices.append((row, col))
            return (row, col)
        model = types.SimpleNamespace(rowCount=lambda: 1, columnCount=lambda: 4, index=index)
        rect = types.SimpleNamespace(x=lambda: 0, y=lambda: 0, width=lambda: 100, height=lambda: 20)
        view = types.SimpleNamespace(model=lambda: model, scrollTo=lambda value: None, visualRect=lambda value: rect)
        runtime = {"test": Reporter(), "mouseClick": lambda *args: clicks.append(args),
                   "Qt": types.SimpleNamespace(NoModifier=0, LeftButton=1)}
        self.assertTrue(loc.click_first_log_row(view, runtime))
        self.assertEqual(indices, [(0, 1)])
        self.assertEqual(clicks[0][1:3], (50, 10))


if __name__ == "__main__":
    unittest.main()
