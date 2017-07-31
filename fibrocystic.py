from easygui import choicebox, multenterbox, msgbox, multchoicebox
import time
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
import pyperclip


def main():

        out_string = "Fibrocystic changes including"
        msg = "Select all that apply"
        title = "Fibrocystic descriptors"
        choices = ["intraductal hyperplasia", "usual ductal hyperplasia",
                   "adenosis", "sclerosing adenosis", "microcysts",
                   "papillomatosis", "columnar cell change", "apocrine change"]
        choicesvalues = multchoicebox(msg, title, choices)

        out_string = " ".join([out_string, ", ".join(choicesvalues), "and stromal fibrosis"])

        # CALC
        title = "Calcifications"
        msg = "Choose one for calcifications"
        calc_dx = ["YES", "NO", "Do not report"]
        calcbox = choicebox(msg, title, calc_dx)
        if calcbox == "YES":
            out_string = " ".join([out_string, "with calcifications."])
        elif calcbox == "NO":
            out_string = " ".join([out_string, "without calcifications."])
        elif calcbox == "Do not report":
            exit
        print(out_string)
        pyperclip.copy(out_string)
main()
