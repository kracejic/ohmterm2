try:
  from tkinter import *
except:
  try:
      from Tkinter import *
  except:
    print ("Tkinter lib is missing.")
    sys.exit()
from toolTip import *


import tkinter.font






class mainWindow(object):
  """docstring for mainWindow"""
  def __init__(self, root, myType, datastore, settings, ohmterm):
    super(mainWindow, self).__init__()
    self.master = root;
    self.datastore = datastore;
    self.settings = settings;
    self.myType = myType
    self.ohmterm = ohmterm


    if self.myType == "main":
      self.CreateGUI_ComPort()
    self.CreateGUI_List()
    

    self.master.columnconfigure(1, minsize=5)
    self.master.columnconfigure(6000, minsize=5) #mezera na konci
    self.master.columnconfigure(35, weight=1)
    self.master.columnconfigure(95, weight=1)



  def CreateGUI_List(self):
    self.content = Frame(self.master, height=2, bd=1, relief=RAISED)
    self.content.grid(row=200, column=0, sticky=W+E+N+S,  columnspan=1000)
    
    #list a scrollbar
    self.scrollbar = Scrollbar(self.content, command=self.scrollin)
    self.scrollbar.grid(row=200, column=900, sticky=W+E+N+S)
    
    self.font_courier = tkinter.font.Font ( family="Courier New", size=10)
    self.font_courier_bold = tkinter.font.Font ( family="Courier New", size=10, weight='bold')
    self.seznam = Listbox(self.content, takefocus=True,selectmode=EXTENDED) 
    self.seznam.config(font=self.font_courier)
    self.seznam.grid(row=200, column=10, columnspan=890, sticky=W+E+N+S)
    
    #self.seznam.bind('<Double-Button-1>', self.CopyModulName2)
    #self.seznam.bind('<Double-Button-3>', self.CopyModulName3)
    #self.seznam.bind('<Button-2>', self.CopyDebugText)

    self.content.rowconfigure(190, pad=8)
    self.content.rowconfigure(200, weight=1)
    self.content.rowconfigure(500, minsize=2)
    
    self.content.columnconfigure(70, weight=1)
    self.content.columnconfigure(90, weight=1)
    self.content.columnconfigure(110, weight=1)
    self.content.columnconfigure(170, weight=1)
    self.content.columnconfigure(500, minsize=4)


    self.master.rowconfigure(200, weight=1)

    
  def CreateGUI_ComPort(self):
    print ("mainWindow.CreateGUI_ComPort(self)")
    Label(self.master, text="Port:").grid(row=10, column=10)
    self.editboxPort = Entry(self.master, width=3);
    self.editboxPort.insert(0,self.ohmterm.inputer.getAddress());
    self.editboxPort.grid(row=10, column=20)
    ToolTip( self.editboxPort, msg="Enter some port number.", follow=True, delay=1.2)
    
    
    self.buttonPortConnect = Button(self.master, text="Connect", fg="red", bg="#eebbbb", height=0, command=self.connect)
    self.buttonPortConnect.grid(row=10, column=30, padx=5)
    ToolTip( self.buttonPortConnect, msg="Connect to COM Port. If this is blue, app is probably connected.", follow=True, delay=1.2)
    
    self.checkBoxAutoconnect = Checkbutton(self.master, text="Autoconnect")
    self.checkBoxAutoconnect.grid(row=10, column=31)
    ToolTip( self.checkBoxAutoconnect, msg="Autoconnect on start?", follow=True, delay=1.2)
    self.checkConnected()


  def checkConnected(self):
    if self.ohmterm.inputer.getStatus():
        self.buttonPortConnect.config(text="Disconect ("+self.ohmterm.inputer.getKind()+")", fg="black", bg="#55dd55")
        return True
    else:
        self.buttonPortConnect.config(text="Connect ("+self.ohmterm.inputer.getKind()+")", fg="red", bg="#eebbbb")
        return False

  def connect(self):
    if self.checkConnected():
        self.ohmterm.inputer.close()
    else:
        self.ohmterm.inputer.open(self.editboxPort.get())
    
    self.checkConnected()






  def scrollin(self, *args): #scroll handling
    self.seznam.yview(*args)

  def addLines(self, lines):
    pass

  def kill(self):
    self.settings[self.myType]["geometry"] = self.master.geometry()

    self.master.destroy()

