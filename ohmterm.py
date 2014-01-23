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

import inputSerial
import inputUDP
import inputTester
import filter
import mainWindow




version1 = 2
version2 = 0
version3 = 0
betaFlag = True







class OhmTerm(object):
  """docstring for OhmTerm"""
  datastore = []
  settingsFileName = "config.ini"


  def __init__(self):
    print ("OhmTerm.__init__(self)")
    super(OhmTerm, self).__init__()

    self.settings = configparser.ConfigParser()
    self.settings.read(self.settingsFileName)

    #creating input
    self.inputer = inputTester.InputTester()


    self.root = Tk()
    self.root.protocol("WM_DELETE_WINDOW", self.killProgram)
    # self.root.geometry("1150x900")
    self.root.geometry(self.settings.get('main', 'geometry', fallback='1150x900') )


    #creating mainwindow
    self.mainwindow = mainWindow.mainWindow(self.root, "main", self.datastore, self.settings, self)



    self.root.mainloop()
    pass


    
  def killProgram(self):
    print ("OhmTerm.killProgram()")
    self.mainwindow.kill()

    self.writeConfig()

  def writeConfig(self):
    fil = open(self.settingsFileName, 'w')
    self.settings.write(fil)
    fil.close()


ohmTermApp = OhmTerm()
