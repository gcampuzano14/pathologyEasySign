from easygui import choicebox, multenterbox, msgbox, multchoicebox
import time
from Tkinter import Tk
import pyperclip
r = Tk()
r.withdraw()
r.clipboard_clear()


def main():
    msgbox("Breast Dx Tool by GCZ and CLL", "Credits", "let's start!")
    # Casetype
    title = "TYPE OF DX"
    msg = "Choose a disease category"
    dx = ["INVASIVE", "INSITU", "FIBROCYSTIC"]
    diagnosis = choicebox(msg, title, dx)
    if diagnosis == "INVASIVE":
        out_string = inv()
    elif diagnosis == "INSITU":
        out_string = insitu()

    elif diagnosis == "FIBROCYSTIC":
        out_string = fcy()
    copypaste(out_string)


def inv():

    out_string = "INVASIVE"

    # TYPE
    title = "TYPE OF MAMMARY CA"
    msg = "Choose a type"
    dx = ["DUCTAL", "LOBULAR", "MAMMARY"]
    diagnosis = choicebox(msg, title, dx)

    if diagnosis == "DUCTAL":
        out_string = "".join([out_string, " DUCTAL CARCINOMA"])
    elif diagnosis == "LOBULAR":
        out_string = "".join([out_string, " LOBULAR CARCINOMA"])
    elif diagnosis == "MAMMARY":
        out_string = "".join([out_string, " MAMMARY CARCINOMA"])

    # TUBULES

    msg = "Calculate grade"
    title = "GRADE CALC"
    fieldNames = ["TUBULES", "NUCLEAR GRADE", "MITOSIS"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title, fieldNames)

    grade_calc = int(fieldValues[0]) + int(fieldValues[1]) + int(fieldValues[2])
    grade_str = " (%s+%s+%s=%s), " % (fieldValues[0], fieldValues[1], fieldValues[2],str(grade_calc))
    if grade_calc == 3 or grade_calc == 4 or grade_calc == 5:
        out_string = "".join([out_string, " WELL DIFFERENTIATED, NOTTINGHAM GRADE 1"])
    elif grade_calc == 6 or grade_calc == 7:
        out_string = "".join([out_string, " MODERATELY DIFFERENTIATED, NOTTINGHAM GRADE 2"])
    elif grade_calc == 8 or grade_calc == 9:
        out_string = "".join([out_string, " POORLY DIFFERENTIATED, NOTTINGHAM GRADE 3"])
    out_string = "".join([out_string, grade_str])

    # TUMOR SIZE
    msg = "TUMOR SIZE IN CM"
    title = "TUMOR SIZE"
    fieldName = ["TUMOR SIZE (cm)"]
    fieldValue = []  # we start with blanks for the values
    fieldValue = multenterbox(msg, title,  fieldName)
    size_str = "%s CM IN GREATEST LINEAR MICROSCOPIC DIMENSION.\n\n" % (fieldValue[0])
    out_string = "".join([out_string, size_str])

    # POS CORES
    msg = "Count cores"
    title = "CORE CALC"
    fieldNames = ["NUMBER OF POSITIVE ", "TOTAL CORES", "PERCENTAGE OF TUMOR"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title,  fieldNames)
    core_str = "THE INVASIVE CARCINOMA IS PRESENT IN %s OF %s CORE FRAGMENTS, REPRESENTING APPROXIMATELY %s%% OF THE TISSUE SAMPLED.\n\n" % (fieldValues[0], fieldValues[1], fieldValues[2])
    out_string = "".join([out_string, core_str])

    # e-cadherin?
    title = "E-CADHERIN"
    msg = "NEEDS E-CADHERIN?"
    dx = ["YES", "NO"]
    need = choicebox(msg, title, dx)
    if need == "YES":
        out_string = "".join([out_string, "IMMUNOHISTOCHEMISTRY FOR ER, PR, HER2 AND E-CADHERIN IS PENDING; AN ADDENDUM TO FOLLOW.\n\n"])
    elif need == "NO":
        out_string = "".join([out_string, "IMMUNOHISTOCHEMISTRY FOR ER, PR AND HER2 IS PENDING; AN ADDENDUM TO FOLLOW.\n\n"])
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


def insitu():

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
        out_string = ", ".join([out_string, "LOW NUCLEAR GRADE"])
    elif grade_box == "INTERMEDIATE":
        out_string = ", ".join([out_string, "INTERMEDIATE NUCLEAR GRADEi"])
    elif grade_box == "HIGH":
        out_string = ", ".join([out_string, "HIGH NUCLEAR GRADE"])

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
        pass

    # TYPES
    if diagnosis == "MAMMARY":
        pass
    else:
        msg = "Select all that apply"
        title = "INSITU TYPES"
        choices = ["SOLID", "CRIBRIFORM", "PAPILLARY", "MICROPAPILLARY", "COMEDO", "PLEOMORPHIC", "APOCRINE"]
        choicesvalues = multchoicebox(msg, title, choices)
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
        out_string = " ".join([out_string, "WITH ASSOCIATED CALCIFICATIONS.\n\n"])
    elif calcbox == "YES WITH NECROSIS":
        out_string = " ".join([out_string, "WITH ASSOCIATED NECROSIS AND CALCIFICATIONS.\n\n"])
    elif calcbox == "NO":
        out_string = " ".join([out_string, "WITHOUT CALCIFICATIONS.\n\n"])
    elif calcbox == "NO with necrosis":
        out_string = " ".join([out_string, "WITH ASSOCIATED NECROSIS.\n\n"])
    elif calcbox == "Do not report":
        pass

    # TUMOR SIZE
    msg = "SIZE"
    title = "TUMOR SIZE"
    fieldName = ["TUMOR SIZE (cm)", "TUMOR PERCENTAGE"]
    fieldValue = []  # we start with blanks for the values
    fieldValue = multenterbox(msg, title,  fieldName)
    size_str = "%s CM IN GREATEST LINEAR MICROSCOPIC DIMENSION, AND REPRESENTING APPROXIMATELY %s%%  OF THE SPECIMEN\n\n" %  (fieldValue[0],fieldValue[1])
    out_string = "".join([out_string, size_str])

    # e-cadherin?
    title = "E-CADHERIN"
    msg = "NEEDS E-CADHERIN?"
    dx = ["YES", "NO"]
    need = choicebox(msg, title, dx)
    if need == "YES":
        out_string = "".join([out_string, "IMMUNOHISTOCHEMISTRY FOR ER, PR AND E-CADHERIN IS PENDING; AN ADDENDUM TO FOLLOW.\n\n"])
    elif need == "NO":
        out_string = "".join([out_string, "IMMUNOHISTOCHEMISTRY FOR ER, PR IS PENDING; AN ADDENDUM TO FOLLOW.\n\n"])

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


def fcy():
    # fibrocystic
    out_string = "FIBROCYSTIC CHANGES INCLUDING"
    msg = "Select all that apply"
    title = "Fibrocystic descriptors"
    choices = ["INTRADUCTAL HYPERPLASIA", "USUAL DUCTAL HYPERPLASIA", "ADENOSIS", "SCLEROSING ADENOSIS", "MICROCYSTS", "PAPILLOMATOSIS", "COLUMNAR CELL CHANGE", "APOCRINE CHANGE"]
    choicesvalues = multchoicebox(msg, title, choices)
    out_string = " ".join([out_string, ", ".join(choicesvalues), "AND STROMAL FIBROSIS"])

    # CALC
    title = "Calcifications"
    msg = "Choose one for calcifications"
    calc_dx = ["YES", "NO", "Do not report"]
    calcbox = choicebox(msg, title, calc_dx)
    if calcbox == "YES":
        out_string = " ".join([out_string, "WITH CALCIFICATIONS."])
    elif calcbox == "NO":
        out_string = " ".join([out_string, "WITHOUT CALCIFICATIONS."])
    elif calcbox == "Do not report":
        pass
    return out_string


def attending(out_string, site):
    date = time.strftime("%m/%d/%Y")

    msg = "SITE DOCTORS"
    title = "SITE"
    fieldNames = ["PATHOLOGIST", "CLINICIAN", "DATE"]
    fieldValues = [" ", " ", str(date)]
    fieldValues = multenterbox(msg, title,  fieldNames, fieldValues)

    people_str = "Dr. %s has reviewed select slides and concurs with the above diagnosis.\n\n" \
    "Dr. %s was notified of the above findings on %s by email. " % (fieldValues[0], fieldValues[1],str(fieldValues[2]))
    out_string = "".join([out_string, people_str])
    if site == "UM":
        out_string = "".join([out_string, "XXX were copied on this communication."])
    elif site == "JMH":
        out_string = "".join([out_string, "XXX were copied on this communication."])
        return out_string
    return out_string


def copypaste(testvar):
    print(testvar)
    pyperclip.copy(testvar)

main()
