try:
    from tkinter import *
except:
    try:
        from Tkinter import *
    except:
        print ("Tkinter lib is missing.")
        sys.exit()

        
def defaultEditBox(widg):
    widg.config(bg="#FFFFFF",relief=FLAT,width=10)
def defaultLabel(widg):
    widg.config(bg="#EEE")
def defaultButton(widg):
    widg.config(bg="#EEE", relief=RAISED,bd=1)
    widg.grid( padx=1, pady=2)
def defaultFrameClean(widg):
    # widg.config(bg="#EEE",relief=SUNKEN)
    widg.config(bg="#EEE",relief=FLAT)
def defaultCheckBox(widg):
    widg.config(bg="#EEE",relief=FLAT,highlightbackground="#EEE")
def defaultListBox(widg):
    widg.config(bg="#FFFFFF")
