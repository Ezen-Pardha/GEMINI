# -*- coding: utf-8 -*-

import names, subprocess, xml.etree.ElementTree as ET, builtins, re, html

import os
 
TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
EXCEL_PATH = os.path.abspath(
    os.path.join( TESTCASE_DIR,
        "..",
        "shared",
        "testdata",
        "Gemini Split strings.xlsx"
    )
)
SHEET_NAME, LANGUAGE, LANG_COL = "settings", "Italian", 14


def norm(x):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(str(x or "")))).strip().casefold()


def texts(o):
    r = []
    try:
        if not o.visible:
            return r
    except Exception:
        pass
    for a in ("text", "title"):
        try:
            v = str(getattr(o, a))
            if v and v not in ("None", "<PyQt5...>"):
                r.append(v)
        except Exception:
            pass
    try:
        for c in object.children(o):
            r += texts(c)
    except Exception:
        pass
    return r


def unzip(m):
    p = subprocess.Popen(["unzip", "-p", EXCEL_PATH, m], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    d, e = p.communicate()
    if p.returncode:
        raise Exception("Cannot read Excel file: " + m)
    return d


def col(r):
    n = 0
    for c in r:
        if not c.isalpha():
            break
        n = n * 26 + ord(c.upper()) - 64
    return n


def excel():
    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    rs = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    wb = ET.fromstring(unzip("xl/workbook.xml"))
    rel = ET.fromstring(unzip("xl/_rels/workbook.xml.rels"))
    links = {x.attrib["Id"]: x.attrib["Target"] for x in rel}
    s = next(x for x in wb.find("{%s}sheets" % ns) if x.attrib["name"] == SHEET_NAME)
    t = links[s.attrib["{%s}id" % rs]].replace("\\", "/").lstrip("/")
    if not t.startswith("xl/"):
        t = "xl/" + t
    root = ET.fromstring(unzip(t))
    ss = []
    try:
        r = ET.fromstring(unzip("xl/sharedStrings.xml"))
        ss = ["".join(x.text or "" for x in item.iter("{%s}t" % ns)) for item in r.findall("{%s}si" % ns)]
    except Exception:
        pass
    rows = {}
    for row in root.findall(".//{%s}sheetData/{%s}row" % (ns, ns)):
        v = {}
        for c in row.findall("{%s}c" % ns):
            typ, node = c.attrib.get("t"), c.find("{%s}v" % ns)
            x = "".join(y.text or "" for y in c.iter("{%s}t" % ns)) if typ == "inlineStr" else (node.text if node is not None else "")
            if typ == "s" and x:
                x = ss[builtins.int(x)]
            v[col(c.attrib["r"])] = str(x).strip()
        rows[builtins.int(row.attrib["r"])] = v
    return rows


def expected():
    rows, start, result = excel(), None, []
    for i in sorted(rows):
        if "system information" in norm(rows.get(i, {}).get(2, "")) and "fiber information" in norm(rows.get(i + 5, {}).get(2, "")):
            start = i
            break
    if start is None:
        return [("System/Fiber Information string #{}".format(i + 1), "", "System/Fiber Information block not found in Excel sheet '{}'.".format(SHEET_NAME)) for i in range(10)]
    for j in range(10):
        rn, row = start + j, rows.get(start + j, {})
        eng, want = str(row.get(2, "")).strip(), str(row.get(LANG_COL, "")).strip()
        error = "Excel row {} is missing.".format(rn) if not row else ("English source string missing in row {}.".format(rn) if not eng else ("Italian translation missing in Excel column N, row {}.".format(rn) if not want else ""))
        result.append((eng, want, error))
    return result


def verify(actual):
    try:
        exp = expected()
    except Exception as e:
        test.fail("FAIL | Excel validation could not be loaded: {}".format(e))
        return
    s = [norm(x) for x in actual if norm(x)]
    combined = norm(" ".join(actual))
    for i, (eng, want, error) in enumerate(exp, 1):
        label = eng or "String #{}".format(i)
        if error:
            test.fail("FAIL | English: {} | Reason: {}".format(label, error))
            continue
        w = norm(want)
        found = any(x == w or (len(w) >= 4 and w in x) for x in s) or (len(w) >= 4 and w in combined)
        if not found and i == 10:
            parts = [norm(x) for x in want.split(":") if norm(x)]
            found = len(parts) >= 2 and all(any(x in z for z in s) for x in parts)
        test.verify(found, "PASS | English: {} | Italian: {}".format(eng, want) if found else "FAIL | English: {} | Expected Italian: {} | Reason: Translation exists in Excel but matching GUI text was not found.".format(eng, want))


def main():
    startApplication("bravo --disable-watchdog --watchdog-timeout=10 --disable-integrity-check --disable-fiber-use-check --disable-firmware-check --disable-ssm --disable-ports-check")
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 460, 105, 924, 127)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 48, 88, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 48, 88, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbItaly_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    snooze(2)
    r = waitForObject(names.o_ScreenSwitcher)
    a = texts(r)
    openContextMenu(waitForObject(names.gbSystemInformation_lbSystemInformation_QLabel), 314, 25, 1)
    snooze(1)
    a += texts(r)
    openContextMenu(waitForObject(names.wdSystemInfoLayout_gbFiberInformation_QGroupBox), 239, 45, 1)
    snooze(1)
    a += texts(r)
    verify(a)
    test.vp("Info Screen Verification")