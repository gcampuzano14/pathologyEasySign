from easygui import choicebox, multenterbox
import time
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
import pyperclip


def main():
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
    grade_str = " (%s+%s+%s=%s), " % (fieldValues[0], fieldValues[1], fieldValues[2], str(grade_calc))
    if grade_calc == 3 or grade_calc == 4 or grade_calc == 5:
        out_string = "".join([out_string, " well differentiated, Nottingham grade 1"])
    elif grade_calc == 6 or grade_calc == 7:
        out_string = "".join([out_string, " moderately differentiated, Nottingham grade 2"])
    elif grade_calc == 8 or grade_calc == 9:
        out_string = "".join([out_string, " poorly differentiated, Nottingham grade 3"])
    out_string = "".join([out_string, grade_str])

    # TUMOR SIZE
    msg = "TUMOR SIZE IN CM"
    title = "TUMOR SIZE"
    fieldName = ["TUMOR SIZE (cm)"]
    fieldValue = []  # we start with blanks for the values
    fieldValue = multenterbox(msg, title, fieldName)

    size_str = "%s cm in greatest linear microscopic dimension.\n\n" %  (fieldValue[0])
    out_string = "".join([out_string, size_str])

    # POS CORES
    msg = "Count cores"
    title = "CORE CALC"
    fieldNames = ["NUMBER OF POSITIVE ", "TOTAL CORES", "PERCENTAGE OF TUMOR"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title, fieldNames)

    core_str = "The invasive carcinoma is present in %s of %s core fragments, representing approximately %s%% of the tissue sampled.\n\n" % (fieldValues[0],fieldValues[1],fieldValues[2])

    out_string = "".join([out_string, core_str])

    # e-cadherin?
    title = "E-CADHERIN"
    msg = "NEEDS E-CADHERIN?"
    dx = ["YES", "NO"]
    need = choicebox(msg,title,dx)
    if need == "YES":
        out_string = "".join([out_string, "Immunohistochemistry for ER, PR, HER2 and E-cadherin is pending; an addendum to follow.\n\n"])
    elif need == "NO":
        out_string = "".join([out_string, "Immunohistochemistry for ER, PR and HER2 is pending; an addendum to follow.\n\n"])

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

    print(out_string)
    pyperclip.copy(out_string)


def attending(out_string, site):
    date = time.strftime("%m/%d/%Y")
    msg = "SITE DOCTORS"
    title = "SITE"
    fieldNames = ["PATHOLOGIST", "CLINICIAN", "DATE"]
    fieldValues = [" ", " ", str(date)]
    fieldValues = multenterbox(msg, title, fieldNames, fieldValues)

    people_str = "Dr. %s has reviewed select slides and concurs with the above diagnosis.\n\n" \
    "Dr. %s was notified of the above findings on %s by email. " % (fieldValues[0],fieldValues[1],str(fieldValues[2]))
    out_string = "".join([out_string, people_str])
    if site == "UM":
        out_string = "".join([out_string, "SO and SO were copied on this communication."])
    elif site == "JMH":
        out_string = "".join([out_string, "SO and SO were copied on this communication."])
        return out_string
    return out_string

main()
