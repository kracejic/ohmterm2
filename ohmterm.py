#! python3
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
from tkinter import messagebox
from tkinter import filedialog

import inputStrategy
import decomposer
import mainWindow
import traceback
import imp
import os










class OhmTerm(object):
    """docstring for OhmTerm"""
    version1 = 2
    version2 = 0
    version3 = 2
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
        self.windows = [self.mainwindow]

        self.loadPlugins()

        self.root.after(1000, self.inputTask)
        self.root.mainloop()
        pass


    def inputTask(self):
        # print ("OhmTerm.inputTask()")
        try:
            rawData = self.inputer.getData()
            decomposedData = self.decomposer.decompose(rawData)
            self.datastore = self.datastore + decomposedData
            self.pushDataToWindow(decomposedData, self.mainwindow)
        except Exception as ex:
            print("ERROR")
            traceback.print_exc()
        self.root.after(50, self.inputTask)
        pass


    def pushDataToWindow(self, data, window):
        for item in data:
            window.insertData(item)


    def deleteDatastore(self):
        print ("OhmTerm.deleteDatastore")
        self.datastore[:] = []
        

    def allWindowsLookAtTop(self):
        for win in self.windows:
            win.LookAtTheTop()
    def refreshAllWindowsAll(self):
        for win in self.windows:
            self.refreshAll(win)
    def refreshAll(self, window):
        print ("OhmTerm.refreshAll - " + window.myType)
        self.pushDataToWindow(self.datastore, window)


    def refreshAllWindowsQuick(self):
        for win in self.windows:
            self.refreshQuick(win)
    def refreshQuick(self, window):
        print ("OhmTerm.refreshQuick - " + window.myType)
        count = 0
        countShowed = 0
        for item in reversed(self.datastore):
            if window.insertDataAtTheStart(item):
                countShowed = countShowed + 1
            count = count + 1
            if count > 10000:
              break
            if countShowed > 500:
              break

        
    def killProgram(self):
        print ("OhmTerm.killProgram()")
        self.inputer.close()
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
        self.createSettingsIfNotExisted("FilterCurrentmain")


    def saveDatastore(self):
        # filename = tkfiledialog.asksaveasfilename(defaultextension="hterm", title="Save as (all)", initialdir=self.savepath)
        filename = filedialog.asksaveasfilename(defaultextension="log", title="Save as (all)")
        if filename == '':
            return

        print ("OhmTerm.saveDatastore - Saving to: " + filename)
        # print ('\nWriting output to '+ output_filename)
        outputh = open(filename,'w')  
        for line in self.datastore :
            outputh.write( line[2] + '\n' )
        outputh.close()
        print (' ... done\n')
        self.savepath = filename
        
        return



    def loadPlugins(self):
        PluginFolder = "./plugins"
        MainModule = "initPlugin"

        self.plugins = {}

        possibleplugins = os.listdir(PluginFolder)
        for i in possibleplugins:
            location = os.path.join(PluginFolder, i)
            if  location.endswith(".py"):
                # print ("Plugins: " + location)
                print ("Plugins: " + i.strip(".py"))
                foundPlugin = imp.find_module(i.strip(".py"), [PluginFolder])
                print(str(foundPlugin))
                name = i.strip(".py")
                self.plugins[name] = {"foundPlugin": foundPlugin}

                #loading plugin
                loadedPlugin = imp.load_module(i.strip(".py"), foundPlugin[0], "./plugins", foundPlugin[2])
                self.plugins[name] ["loadedPlugin"] = loadedPlugin

                #init of plugin
                loadedPlugin.initPluginPost(self)




ohmTermApp = OhmTerm()
