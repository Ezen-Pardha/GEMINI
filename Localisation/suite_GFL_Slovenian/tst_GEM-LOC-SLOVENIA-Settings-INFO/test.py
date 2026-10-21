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
SHEET_NAME, LANGUAGE, LANG_COL = "settings", "Slovenian", 23

def norm(x):
    x = html.unescape(str(x or ""))
    x = re.sub(r"<[^>]+>", " ", x)
    return re.sub(r"\s+", " ", x).strip().casefold()

def texts(o):
    r = []
    try:
        if not o.visible:
            return r
    except:
        pass
    for a in ("text", "title"):
        try:
            v = str(getattr(o, a))
            if v and v not in ("None", "<PyQt5...>"):
                r.append(v)
        except:
            pass
    try:
        for c in object.children(o):
            r += texts(c)
    except:
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
    sheet = next(x for x in wb.find("{%s}sheets" % ns) if x.attrib["name"] == SHEET_NAME)
    target = links[sheet.attrib["{%s}id" % rs]].replace("\\", "/").lstrip("/")
    if not target.startswith("xl/"):
        target = "xl/" + target
    root = ET.fromstring(unzip(target))
    shared = []
    try:
        data = ET.fromstring(unzip("xl/sharedStrings.xml"))
        shared = ["".join(x.text or "" for x in item.iter("{%s}t" % ns)) for item in data.findall("{%s}si" % ns)]
    except:
        pass
    rows = {}
    for row in root.findall(".//{%s}sheetData/{%s}row" % (ns, ns)):
        values = {}
        for cell in row.findall("{%s}c" % ns):
            typ = cell.attrib.get("t")
            node = cell.find("{%s}v" % ns)
            value = "".join(x.text or "" for x in cell.iter("{%s}t" % ns)) if typ == "inlineStr" else (node.text if node is not None else "")
            if typ == "s" and value:
                value = shared[builtins.int(value)]
            values[col(cell.attrib["r"])] = str(value).strip()
        rows[builtins.int(row.attrib["r"])] = values
    return rows

def expected():
    rows = excel()
    for i in sorted(rows):
        block = [rows.get(i + j) for j in range(10)]
        if any(x is None for x in block):
            continue
        english = [str(x.get(2, "")).strip() for x in block]
        if "system information" in norm(english[0]) and "fiber information" in norm(english[5]):
            result = [(english[j], str(block[j].get(LANG_COL, "")).strip()) for j in range(10)]
            missing = [str(j + 1) for j, (e, t) in enumerate(result) if not e or not t]
            if missing:
                raise Exception("Missing English or Slovenian translation in Excel column W for string(s): " + ", ".join(missing))
            return result
    raise Exception("System/Fiber Information strings not found")

def verify(actual):
    try:
        exp = expected()
    except Exception as e:
        test.fail("Slovenian Excel verification error: " + str(e))
        return
    strings = [norm(x) for x in actual if norm(x)]
    combined = norm(" ".join(actual))
    for i, (eng, want) in enumerate(exp):
        w = norm(want)
        found = any(x == w or (len(w) >= 4 and w in x) for x in strings) or (len(w) >= 4 and w in combined)
        if not found and i == 9:
            parts = [norm(x) for x in want.split(":") if norm(x)]
            found = len(parts) >= 2 and all(any(part in text for text in strings) for part in parts)
        test.verify(found, "PASS | English: " + eng + " | Slovenian: " + want if found else "FAIL | English: " + eng + " | Expected Slovenian: " + want + " | Actual text not found")

def main():
    startApplication("bravo --disable-watchdog --watchdog-timeout=10 --disable-integrity-check --disable-fiber-use-check --disable-firmware-check --disable-ssm --disable-ports-check")
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 462, 164, 1124, 185)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 84, 65, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 84, 70, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbSlovenia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    snooze(2)
    r = waitForObject(names.o_ScreenSwitcher)
    a = texts(r)
    openContextMenu(waitForObject(names.wdSystemInfoLayout_gbSystemInformation_QGroupBox), 473, 56, 1)
    snooze(1)
    a += texts(r)
    openContextMenu(waitForObject(names.gbFiberInformation_lbFiberInformation_QLabel), 284, 29, 1)
    snooze(1)
    a += texts(r)
    sendEvent("QMouseEvent", waitForObject(names.gbFiberInformation_lbFiberInformation_QLabel), QEvent.MouseButtonDblClick, 284, 29, Qt.RightButton, 3, 0)
    sendEvent("QMouseEvent", waitForObject(names.gbFiberInformation_lbFiberInformation_QLabel), QEvent.MouseButtonRelease, 284, 29, Qt.RightButton, 1, 0)
    a += texts(r)
    verify(a)
    test.vp("Info screen Verification")