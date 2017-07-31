from easygui import choicebox, multenterbox, msgbox, multchoicebox
import time
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
import pyperclip

msgbox("Making your life easy courtesy of German Campuzano and Cesar A Llanos", "Credits", "let's start")


def main():
    # TYPE
    title = "TYPE OF MAMMARY INSITU"
    msg = "Choose a type of In Situ"
    dx = ["DUCTAL", "LOBULAR", "MAMMARY"]
    diagnosis = choicebox(msg, title, dx)

    out_string = ""

    if diagnosis == "DUCTAL":
        out_string = "".join([out_string, " DUCTAL CARCINOMA IN SITU"])
    elif diagnosis == "LOBULAR":
        out_string = "".join([out_string, " LOBULAR CARCINOMA IN SITU"])
    elif diagnosis == "MAMMARY":
        out_string = "".join([out_string, " MAMMARY CARCINOMA IN SITU"])

    # GRADE
    title = "GRADE"
    msg = "PICK GRADE OF INSITU"
    gr = ["LOW", "INTERMEDIATE", "HIGH"]
    grade_box = choicebox(msg, title, gr)

    if grade_box == "LOW":
        out_string = ", ".join([out_string, "low nuclear grade"])
    elif grade_box == "INTERMEDIATE":
        out_string = ", ".join([out_string, "intermediate nuclear grade"])
    elif grade_box == "HIGH":
        out_string = ", ".join([out_string, "high nuclear grade"])

    if diagnosis == "DUCTAL" and grade_box == "LOW":
        out_string = " ".join([out_string, "(DIN 1)"])
    elif diagnosis == "DUCTAL" and grade_box == "INTERMEDIATE":
        out_string = " ".join([out_string, "(DIN 2)"])
    elif diagnosis == "DUCTAL" and grade_box == "HIGH":
        out_string = " ".join([out_string, "(DIN 3)"])
    elif diagnosis == "LOBULAR" and grade_box == "LOW":
        out_string = " ".join([out_string, "(LIN 1)"])
    elif diagnosis == "LOBULAR" and grade_box == "INTERMEDIATE":
        out_string = " ".join([out_string, "(LIN 2)"])
    elif diagnosis == "LOBULAR" and grade_box == "HIGH":
        out_string = " ".join([out_string, "(LIN 3)"])
    elif diagnosis == "MAMMARY":
        exit

    # TYPES
    if diagnosis == "MAMMARY":
        exit
    else:
        msg = "Select all that apply"
        title = "INSITU TYPES"
        choices = ["solid", "cribriform", "papillary", "micropapillary", "comedo", "pleomorphic", "apocrine"]
        choicesvalues = multchoicebox (msg, title, choices)
        print(len(choicesvalues))
        if len(choicesvalues) > 1:
            out_string = " ".join([out_string, ", ".join(choicesvalues[:-1]), "and", "".join(choicesvalues[-1]), "types,"])
        else:
            out_string = " ".join([out_string, ", ".join(choicesvalues), "type,"])

    # CALC
    title = "Calcifications"
    msg = "Choose one for calcifications"
    calc_dx = ["YES", "YES WITH NECROSIS", "NO", "NO with necrosis", "Do not report"]
    calcbox = choicebox(msg, title, calc_dx)
    if calcbox == "YES":
        out_string = " ".join([out_string, "with associated calcifications.\n\n"])
    elif calcbox == "YES WITH NECROSIS":
        out_string = " ".join([out_string, "with associated necrosis and calcifications.\n\n"])
    elif calcbox == "NO":
        out_string = " ".join([out_string, "without calcifications.\n\n"])
    elif calcbox == "NO with necrosis":
        out_string = " ".join([out_string, "with associated necrosis.\n\n"])
    elif calcbox == "Do not report":
        exit

    # TUMOR SIZE
    msg = "SIZE"
    title = "TUMOR SIZE"
    fieldName = ["TUMOR SIZE (cm)", "TUMOR PERCENTAGE"]
    fieldValue = []  # we start with blanks for the values
    fieldValue = multenterbox(msg, title,  fieldName)
    size_str = "%s cm in greatest linear microscopic dimension, and representing approximately %s%%  of the specimen\n\n" %  (fieldValue[0],fieldValue[1])
    out_string = "".join([out_string, size_str ])

    # e-cadherin?
    title = "E-CADHERIN"
    msg = "NEEDS E-CADHERIN?"
    dx = ["YES", "NO"]
    need = choicebox(msg, title, dx)
    if need == "YES":
        out_string = "".join([out_string, "Immunohistochemistry for ER, PR and E-cadherin is pending; an addendum to follow.\n\n"])
    elif need == "NO":
        out_string = "".join([out_string, "Immunohistochemistry for ER, PR is pending; an addendum to follow.\n\n"])

    print(out_string)
    pyperclip.copy(out_string)

    title = "DIAGNOSIS"
    msg = "NEW DIAGNOSIS?"
    dx = ["YES", "NO"]
    new_dx = choicebox(msg, title, dx)

    if new_dx == "YES":
        title = "DIAGNOSIS SITE"
        msg = "Choose site"
        dx = ["JMH", "UM"]
        site_dx = choicebox(msg, title, dx)
        if site_dx == "JMH":
            out_string = attending(out_string, site_dx)

        elif site_dx == "UM":
            out_string = attending(out_string, site_dx)
    return out_string

    print(out_string)
    pyperclip.copy(out_string)

main()
