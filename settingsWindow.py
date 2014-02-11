try:
    from tkinter import *
except:
    try:
        from Tkinter import *
    except:
        print ("Tkinter lib is missing.")
        sys.exit()



class SettingsWindow(Toplevel):
    """docstring for SettingsWindow"""
    def __init__(self, settings):
        Toplevel.__init__(self)
        # super(SettingsWindow, self).__init__()
        self.settings = settings
        self.title("Ohmterm2 - Settings")
        self.geometry(self.settings.get('main', 'settingsGeometry', fallback='480x320') )


        self.protocol("WM_DELETE_WINDOW", self.killWindow)


    def killWindow(self):
        self.settings['main']['settingsGeometry'] = self.geometry()
        self.destroy()








