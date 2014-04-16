try:
    from tkinter import *
except:
    try:
        from Tkinter import *
    except:
        print ("Tkinter lib is missing.")
        sys.exit()
from defaultSkin import *



class SettingsWindow(Toplevel):
    """docstring for SettingsWindow"""
    def __init__(self, settings, ohmterm):
        Toplevel.__init__(self)
        # super(SettingsWindow, self).__init__()
        self.settings = settings
        self.ohmterm = ohmterm
        self.title("Ohmterm2 - Settings")
        self.geometry(self.settings.get('main', 'settingsGeometry', fallback='480x320') )
        defaultFrameClean(self)


        self.protocol("WM_DELETE_WINDOW", self.killWindow)


        self.frameInput = Frame(self, height=64, bd=1)
        defaultFrameDirty(self.frameInput)
        self.frameInput.pack(fill=X)


        LabelInput = Label(self.frameInput, text="Input")
        defaultLabel(LabelInput)
        LabelInput.grid(row = 1, column=1, sticky=W+E )

        LabelComposer = Label(self.frameInput, text="Composer")
        defaultLabel(LabelComposer)
        LabelComposer.grid(row = 2, column=1, sticky=W+E )

        self.editText = StringVar()
        self.editText.set(self.ohmterm.inputer.getStrategy())
        EditInput = OptionMenu(self.frameInput, self.editText, *self.ohmterm.inputer.getAvailableStrategies(), command=self.changeInput )
        defaultOptionMenu(EditInput)
        EditInput.grid(row = 1, column=2, sticky=W+E )

        self.decomposerText = StringVar()
        self.decomposerText.set(self.ohmterm.decomposer.getStrategy())
        Editdecomposer = OptionMenu(self.frameInput, self.decomposerText, *self.ohmterm.decomposer.getAvailableStrategies(), command=self.changeDecomposer )
        defaultOptionMenu(Editdecomposer)
        Editdecomposer.grid(row = 2, column=2, sticky=W+E )

        # self.optionmenu = OptionMenu(master, self.var, *OPTIONS, command=self.menuf)
        # self.optionmenu.grid(row=10, column=40, padx=5)
        # ToolTip( self.optionmenu, msg="Here is the list of current saved presets. To load preset choose preset and press load button. \n Your last session's preset is stored as Last session.", follow=True, delay=1.2)
        
        # self.optionMenuReset()

    def changeInput(self, newType):
        self.ohmterm.inputer.setStrategy(newType)
        self.ohmterm.mainwindow.checkConnected()
        return

    def changeDecomposer(self, newType):
        self.ohmterm.decomposer.setStrategy(newType)
        return

    def killWindow(self):
        self.settings['main']['settingsGeometry'] = self.geometry()
        self.destroy()








