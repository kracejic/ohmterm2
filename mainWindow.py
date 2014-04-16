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
import filter
import settingsWindow
from defaultSkin import *



class mainWindow(object):
    """docstring for mainWindow"""
    def __init__(self, root, myType, datastore, settings, ohmterm):
        super(mainWindow, self).__init__()
        self.master = root;
        self.datastore = datastore;
        self.settings = settings;
        self.myType = myType
        self.ohmterm = ohmterm
        print ("mainWindow.__init__(myType="+myType+")")
        self.master.title("Ohmterm "+self.settings["main"]["version"])
        defaultFrameClean( self.master)


        self.filtr = filter.Filter(settings, self.myType)


        #First Row
        self.frameFirstRow = Frame(height=32, bd=1)
        defaultFrameClean(self.frameFirstRow)
        self.frameFirstRow.grid(row=5, column=10, columnspan=90, sticky=W+E+N+S)
        self.frameFirstRow.columnconfigure(40, weight=1)
        self.frameFirstRow.columnconfigure(60, weight=1)

        #Action Row
        self.frameActionRow = Frame(height=32, bd=1)
        defaultFrameClean(self.frameActionRow)
        self.frameActionRow.grid(row=30, column=10, columnspan=90, sticky=W+E+N+S)
        self.frameActionRow.columnconfigure(40, weight=1)
        self.frameActionRow.columnconfigure(60, weight=1)

        if self.myType == "main":
            self.CreateGUI_ComPort()
        self.CreateGUI_List()

        self.CreateGuiBasic()
        self.CreateGuiActionsBar()
        

        self.master.columnconfigure(1, minsize=5)
        self.master.columnconfigure(6000, minsize=5) #mezera na konci
        self.master.columnconfigure(35, weight=1)
        self.master.columnconfigure(95, weight=1)


        #refresh settings
        self.filtr.loadSettings()

    def CreateGuiBasic(self):
        self.settingsIcon = PhotoImage(file="data/settings.gif")
        self.settingsButton = Button(self.frameFirstRow, image=self.settingsIcon, command=self.showSettings)
        self.settingsButton.grid(row=10, column=100)
        defaultButton(self.settingsButton)
    

    def CreateGuiActionsBar(self):
        self.iconRefresh = PhotoImage(file="data/refresh.gif")
        self.buttonRefresh = Button(self.frameActionRow, text="clear", image=self.iconRefresh, command=self.clear)
        self.buttonRefresh.grid(row=10, column=10)
        defaultButton(self.buttonRefresh)

        self.iconRefreshB = PhotoImage(file="data/refreshB.gif")
        self.buttonRefresh = Button(self.frameActionRow, text="clear", image=self.iconRefreshB, command=self.clear)
        self.buttonRefresh.grid(row=10, column=20)
        defaultButton(self.buttonRefresh)

        self.iconClean = PhotoImage(file="data/clean.gif")
        self.buttonClear = Button(self.frameActionRow, text="clear", image=self.iconClean, command=self.clear)
        self.buttonClear.grid(row=10, column=45)
        defaultButton(self.buttonClear)

        self.iconDelete = PhotoImage(file="data/delete.gif")
        self.buttonDelete = Button(self.frameActionRow, text="clear", image=self.iconDelete, command=self.clear)
        self.buttonDelete.grid(row=10, column=46)
        defaultButton(self.buttonDelete)

        self.iconSave = PhotoImage(file="data/save.gif")
        self.buttonSave = Button(self.frameActionRow, text="clear", image=self.iconSave, command=self.clear)
        self.buttonSave.grid(row=10, column=85)
        defaultButton(self.buttonSave)



    def CreateGUI_List(self):
        self.content = Frame(self.master, height=2, bd=1, relief=RAISED)
        defaultFrameClean(self.content)
        self.content.grid(row=200, column=10, sticky=W+E+N+S,  columnspan=90)
        
        #list a scrollbar
        self.scrollbar = Scrollbar(self.content, command=self.scrollin)
        self.scrollbar.grid(row=200, column=900, sticky=W+E+N+S)
        
        self.font_courier = tkinter.font.Font ( family="Courier New", size=10)
        self.font_courier_bold = tkinter.font.Font ( family="Courier New", size=10, weight='bold')
        self.listView = Listbox(self.content, takefocus=True,selectmode=EXTENDED)
        defaultListBox(self.listView)
        self.listView.grid(row=200, column=10, columnspan=890, sticky=W+E+N+S)
        
        #self.listView.bind('<Double-Button-1>', self.CopyModulName2)
        #self.listView.bind('<Double-Button-3>', self.CopyModulName3)
        #self.listView.bind('<Button-2>', self.CopyDebugText)

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
        lab = Label(self.frameFirstRow, text="Port:")
        lab.grid(row=10, column=10, sticky=N+S)
        defaultLabel(lab)
        self.editboxPort = Entry(self.frameFirstRow, width=3);
        self.editboxPort.insert(0,self.ohmterm.inputer.getAddress());
        self.editboxPort.grid(row=10, column=12)
        defaultEditBox(self.editboxPort)
        ToolTip( self.editboxPort, msg="Enter some port number.", follow=True, delay=1.2)
        
        
        self.buttonPortConnect = Button(self.frameFirstRow, text="Connect", fg="red", bg="#eebbbb", command=self.connect)
        self.buttonPortConnect.grid(row=10, column=14, padx=5)
        defaultButton(self.buttonPortConnect)
        ToolTip( self.buttonPortConnect, msg="Connect to COM Port. If this is blue, app is probably connected.", follow=True, delay=1.2)
        
        self.checkBoxAutoconnect = Checkbutton(self.frameFirstRow, text="Autoconnect")
        self.checkBoxAutoconnect.grid(row=10, column=16, sticky=N+S)
        ToolTip( self.checkBoxAutoconnect, msg="Autoconnect on start?", follow=True, delay=1.2)
        defaultCheckBox(self.checkBoxAutoconnect)
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


    def showSettings(self):
        self.settingsWindow = settingsWindow.SettingsWindow(self.settings, self.ohmterm)

    def clear(self):
        self.listView.delete(0, END)
    def refresh(self):
        # self.ohmterm.refresh()
        pass



    def scrollin(self, *args): #scroll handling
        self.listView.yview(*args)


        # class FilterReturnObject:
        #   colorText = "black"
        #   colorBg = "white"
        #   bold = False
        #   shouldShow = False
    def insertData(self, item):
        print ("mainWindow.insertData data = " + str(item))
        filtered = self.filtr.testLine(item)
        if filtered.shouldShow == True:
                self.listView.insert(END, item[2])
                self.listView.itemconfig(END, fg=filtered.colorText, bg=filtered.colorBg)
        else:
                return False

        return True

    def kill(self):
        self.settings[self.myType]["geometry"] = self.master.geometry()

        self.master.destroy()

