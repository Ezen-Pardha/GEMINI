# -*- coding: utf-8 -*-

import names, subprocess, xml.etree.ElementTree as ET, builtins, re, html

EXCEL_PATH="/home/user/GUI Strings Excel/Gemini Split strings.xlsx"
SHEET_NAME,LANGUAGE="settings","Hungarian"

def norm(x):
    x=html.unescape(str(x or ""))
    x=re.sub(r"<[^>]+>"," ",x)
    return re.sub(r"\s+"," ",x).strip().casefold()

def texts(o):
    r=[]
    try:
        if not o.visible:return r
    except:pass
    for a in ("text","title"):
        try:
            v=str(getattr(o,a))
            if v and v not in ("None","<PyQt5...>"):r.append(v)
        except:pass
    try:
        for c in object.children(o):r+=texts(c)
    except:pass
    return r

def unzip(m):
    p=subprocess.Popen(["unzip","-p",EXCEL_PATH,m],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    d,e=p.communicate()
    if p.returncode:raise Exception("Cannot read Excel file: "+m)
    return d

def col(r):
    n=0
    for c in r:
        if not c.isalpha():break
        n=n*26+ord(c.upper())-64
    return n

def excel():
    ns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    rs="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    wb=ET.fromstring(unzip("xl/workbook.xml"))
    rel=ET.fromstring(unzip("xl/_rels/workbook.xml.rels"))
    links={x.attrib["Id"]:x.attrib["Target"] for x in rel}
    s=next(x for x in wb.find("{%s}sheets"%ns) if x.attrib["name"]==SHEET_NAME)
    t=links[s.attrib["{%s}id"%rs]].replace("\\","/").lstrip("/")
    if not t.startswith("xl/"):t="xl/"+t
    root=ET.fromstring(unzip(t))
    ss=[]
    try:
        r=ET.fromstring(unzip("xl/sharedStrings.xml"))
        ss=["".join(x.text or "" for x in s.iter("{%s}t"%ns))
            for s in r.findall("{%s}si"%ns)]
    except:pass
    rows={}
    for row in root.findall(".//{%s}sheetData/{%s}row"%(ns,ns)):
        v={}
        for c in row.findall("{%s}c"%ns):
            typ=c.attrib.get("t")
            node=c.find("{%s}v"%ns)
            x="".join(y.text or "" for y in c.iter("{%s}t"%ns)) if typ=="inlineStr" else (node.text if node is not None else "")
            if typ=="s" and x:
                x=ss[builtins.int(x)]
            v[col(c.attrib["r"])]=str(x).strip()
        rows[builtins.int(row.attrib["r"])]=v
    return rows

def expected():
    rows=excel()
    lc=13
    for i in sorted(rows):
        b=[rows.get(i+j) for j in range(10)]
        if any(x is None for x in b):
            continue
        e=[str(x.get(2,"")).strip() for x in b]
        if "system information" in norm(e[0]) and "fiber information" in norm(e[5]):
            r=[(e[j],str(b[j].get(lc,"")).strip()) for j in range(10)]
            if all(e and t for e,t in r):
                return r
    raise Exception("System/Fiber Information strings not found")

def verify(a):
    exp=expected()
    s=[norm(x) for x in a if norm(x)]
    c=norm(" ".join(a))
    for i,(eng,want) in enumerate(exp):
        w=norm(want)
        found=any(x==w or (len(w)>=4 and w in x) for x in s) or (len(w)>=4 and w in c)
        if not found and i==9:
            p=[norm(x) for x in want.split(":") if norm(x)]
            found=len(p)>=2 and all(any(x in z for z in s) for x in p)
        test.verify(
            found,
            "English: "+eng+" | Hungarian: "+want if found else
            "English: "+eng+" | Expected: "+want+" | Actual text not found"
        )

def main():
    startApplication("bravo --disable-watchdog --watchdog-timeout=10 --disable-integrity-check --disable-fiber-use-check --disable-firmware-check --disable-ssm --disable-ports-check")
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 460, 105, 924, 127)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 48, 88, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 48, 88, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbHungary_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    snooze(2)
    r=waitForObject(names.o_ScreenSwitcher)
    a=texts(r)
    openContextMenu(waitForObject(names.gbSystemInformation_lbSystemInformation_QLabel),314,25,1)
    snooze(1)
    a+=texts(r)
    openContextMenu(waitForObject(names.wdSystemInfoLayout_gbFiberInformation_QGroupBox),239,45,1)
    snooze(1)
    a+=texts(r)
    verify(a)

    test.vp("Info Screen Verification")
