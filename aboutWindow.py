try:
    from tkinter import *
except:
    try:
        from Tkinter import *
    except:
        print ("Tkinter lib is missing.")
        sys.exit()



class AboutWindow(Toplevel):
    """docstring for AboutWindow"""
    def __init__(self, settings):
        Toplevel.__init__(self)
        # super(AboutWindow, self).__init__()
        self.settings = settings
        self.title("Ohmterm2 - About")
        self.geometry('480x320')

        #Settings
        #Icon made by Freepik from Flaticon.com
        #<div>Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com/free-icon/settings-gear-ios-7-interface-symbol_17214" title="Flaticon">www.flaticon.com</a></div>

        #Ninja
        #Icon made by Freepik from Flaticon.com
        #<div>Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com/free-icon/spy-japanese-ninja_13143" title="Flaticon">www.flaticon.com</a></div>


# <div>Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com/free-icon/arrow-circular-refresh-content-ios-7-interface-symbol_20102" title="Flaticon">www.flaticon.com</a></div>
# <div>Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com/free-icon/arrow-circular-refresh-content-ios-7-interface-symbol_20151" title="Flaticon">www.flaticon.com</a></div>



#for f in *.png; do echo "Converting $f"; convert "$f" -filter Lanczos -sample 32x32 "$(basename "$f" .png).gif"; done
