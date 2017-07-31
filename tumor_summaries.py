from easygui import choicebox, multenterbox, msgbox, multchoicebox,enterbox
import time
from Tkinter import Tk
from win32con import OUT_STRING_PRECIS
r = Tk()
r.withdraw()
r.clipboard_clear()
import pyperclip


def main():
    msgbox("Tumor Summaries by CLL", "Credits", "let's start!")
    # type of tumor summary
    title = "TUMOR SUMMARIES"
    msg = "Choose a synoptic reporting"
    ts = ["Lung", "Breast", "Kidney", "Colon", "Ureter/Renalpelvis"]
    tumorsummary= choicebox(msg, title, ts)
    if tumorsummary == "Lung":
        out_string = lng()
    elif tumorsummary == "Breast":
        out_string = brs()
    elif tumorsummary == "Kidney":
        out_string = kdn()
    elif tumorsummary == "Colon":
        out_string = cln()
    elif tumorsummary == "Ureter/Renalpelvis":
        out_string = urt()
    copypaste(out_string)


def lng():
    out_string = "SURGICAL PATHOLOGY CANCER CASE SUMMARY\n\n"
    msg = ""
    title = "SPECIMEN"
    sp = ["lung", "Lobe(s) of lung", "Bronchus", "Other", "Not specified"]
    specimen = choicebox(msg, title, sp)

    if specimen == "lung":
        out_string = "".join([out_string, "SPECIMEN:LUNG\n"])
    elif specimen == "Lobe(s) of lung":
        msg = "SPECIFY"
        title = ""
        site = ""
        fieldname = "LOBE(S) OF LUNG,"
        fieldValue = []
        fieldValue = enterbox(msg, title, fieldname)
        out_string = "".join([out_string, "SPECIMEN:", fieldValue, "\n"])
    elif specimen == "Bronchus":
        msg = "SPECIFY"
        title = ""
        site = ""
        fieldname = "BRONCHUS,"
        fieldValue = []
        fieldValue = enterbox(msg, title, fieldname)
        out_string = "".join([out_string, "SPECIMEN:", fieldValue, "\n"])
    elif specimen == "Other":
        msg = "SPECIFY"
        title = ""
        site = ""
        fieldname = "OTHER,"
        fieldValue = []
        fieldValue = enterbox(msg, title, fieldname)
        out_string = "".join([out_string, "SPECIMEN:", fieldValue, "\n"])
    elif specimen == "Not specified":
        out_string = "".join([out_string, "SPECIMEN:NOT SPECIFIED\n"])

    msg = ""
    title = "PROCEDURE"
    pr = ["Major airway resection", "Wedge resection", "Segmentectomy", "Lobectomy", "Bilobectomy", "Pneumonectomy", "Other", "Not specified"]
    procedure = choicebox(msg, title, pr)
    if procedure == "Major airway resection":
        out_string = "".join([out_string, "PROCEDURE: MAJOR AIRWAY RESECTION\n"])
    elif procedure == "Wedge resection":
        out_string = "".join([out_string, "PROCEDURE: WEDGE RESECTION\n"])
    elif procedure == "Segmentectomy":
        out_string = "".join([out_string, "PROCEDURE: SEGMENTECTOMY\n"])
    elif procedure == "Lobectomy":
        out_string = "".join([out_string, "PROCEDURE: LOBECTOMY\n"])
    elif procedure == "Bilobectomy":
        out_string = "".join([out_string, "PROCEDURE: BILOBECTOMY\n"])
    elif procedure == "Pneumonectomy":
        out_string = "".join([out_string, "PROCEDURE: PNEUMONECTOMY\n"])
    elif procedure == "Other":
        out_string = "".join([out_string, "PROCEDURE: OTHER\n"])
    elif procedure == "Not specified":
        out_string = "".join([out_string, "PROCEDURE: NOT SPECIFIED\n"])

    msg = ""
    title = "LATERALITY"
    lt = ["Left", "Right", "Not specified"]
    laterality = choicebox(msg, title, lt)
    if laterality == "Left":
        out_string = "".join([out_string, "LATERALITY:LEFT\n"])
    elif laterality == "Right":
        out_string = "".join([out_string, "LATERALITY:RIGHT\n"])
    elif laterality == "Not specified":
        out_string = "".join([out_string, "LATERALITY:NOT SPECIFIED\n"])

    return out_string

out_string = main()
print(out_string)

