import sys
try:
    from tkinter import *
except:
    try:
            from Tkinter import *
    except:
        print ("Tkinter lib is missing.")
        sys.exit()
    
import configparser

import inputStrategy
import decomposer
import mainWindow
import traceback










class OhmTerm(object):
    """docstring for OhmTerm"""
    version1 = 2
    version2 = 0
    version3 = 0
    betaFlag = True

    datastore = []
    settingsFileName = "config.ini"

    mainwindow = None


    def __init__(self):
        print ("OhmTerm.__init__(self)")
        super(OhmTerm, self).__init__()

        self.settings = configparser.ConfigParser()
        self.settings.read(self.settingsFileName)
        self.recreateSettings()
        self.strVersion = str(self.version1) + '.' + str(self.version2) + '.' + str(self.version3)
        if self.betaFlag:
            self.strVersion = self.strVersion + "Beta"
        self.settings["main"]["version"] = self.strVersion
        self.settings["main"]["v1"] = str(self.version1)
        self.settings["main"]["v2"] = str(self.version2)
        self.settings["main"]["v3"] = str(self.version3)
        self.settings["main"]["vBeta"] = str(self.betaFlag)


        #creating input
        self.inputer = inputStrategy.InputStrategy(self.settings)

        #creating decomposer
        self.decomposer = decomposer.Decomposer(self.settings)

        #creating window
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.killProgram)
        self.root.geometry(self.settings.get('main', 'geometry', fallback='1150x900') )
        self.mainwindow = mainWindow.mainWindow(self.root, "main", self.datastore, self.settings, self)
        img = PhotoImage(file='data/ohmterm.gif')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)


        self.root.after(1000, self.inputTask)
        self.root.mainloop()
        pass

    def inputTask(self):
        print ("OhmTerm.inputTask()")
        try:
            rawData = self.inputer.getData()
            decomposedData = self.decomposer.decompose(rawData)
            self.datastore = self.datastore + decomposedData

            #input data to window
            for item in decomposedData:
                self.mainwindow.insertData(item)
        except Exception as ex:
            print("ERROR")
            traceback.print_exc()


        self.root.after(1000, self.inputTask)
        pass

        
        
    def killProgram(self):
        print ("OhmTerm.killProgram()")
        self.mainwindow.kill()
        self.writeConfig()

    def writeConfig(self):
        fil = open(self.settingsFileName, 'w')
        self.settings.write(fil)
        fil.close()


    def createSettingsIfNotExisted(self, paragraph):
        if (paragraph in self.settings) == False:
            print("Creating settings: " + paragraph)
            self.settings[paragraph] = {}

    def recreateSettings(self):
        self.createSettingsIfNotExisted("main")
        self.createSettingsIfNotExisted("input")
        self.createSettingsIfNotExisted("test")
        self.createSettingsIfNotExisted("none")
        self.createSettingsIfNotExisted("udp")
        self.createSettingsIfNotExisted("com")
        self.createSettingsIfNotExisted("FilterDefault")
        self.createSettingsIfNotExisted("FilterCurrentmain")


ohmTermApp = OhmTerm()
