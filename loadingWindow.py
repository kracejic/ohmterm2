try:
    from tkinter import *
except:
    try:
        from Tkinter import *
    except:
        print ("Tkinter lib is missing.")
        sys.exit()
from defaultSkin import *



class LoadingWindow(Toplevel):
    """docstring for LoadingWindow"""
    def __init__(self, ohmterm, lineCount):
        Toplevel.__init__(self)
        # super(LoadingWindow, self).__init__()
        self.lineCount = lineCount
        self.ohmterm = ohmterm
        self.title("Loading file")
        # self.geometry(self.settings.get('main', 'loadingGeometry', fallback='480x320') )
        geometry = self.ohmterm.mainwindow.master.geometry()
        position = geometry.split("+")[1:3]
        size = geometry.split("+")[0].split("x")

        newPosition = [int(position[0]) - 150 +int(int(size[0])/2) , int(position[1]) -100+ int(int(size[1])/2)]
        newPositionStr = "300x80+"+str(newPosition[0])+"+"+str(newPosition[1])
        self.geometry(newPositionStr)
        # print ("G - p:" + str(position))
        # print ("G - s:" + str(size))
        # print ("NNN  :" + str(newPosition))
        # print ("NNN  :" + newPositionStr)
        defaultFrameClean(self)


        self.protocol("WM_DELETE_WINDOW", self.killWindow)


        self.frameInput = Frame(self, bd=1)
        defaultFrameDirty(self.frameInput)
        self.frameInput.pack(fill=BOTH, expand=1)

        self.text = StringVar()
        self.LabelDone = Label(self.frameInput, textvariable=self.text)
        defaultLabel(self.LabelDone)
        self.LabelDone.grid(row = 1, column=1, sticky=W+E )
        self.text.set("0 % done")



    def setCompleted(self, linesDone):
        print("LoadingWindow.setCompleted()" + str(linesDone) + " / " + str(self.lineCount) )
        done = 100.0 * linesDone / self.lineCount
        done = int(done)
        if done > 100:
            done = 100
        # print("LoadingWindow.setCompleted() done = " + str(done))
        self.text.set(str(done)+" % done" )
        return

    def setProgress(self, doneP):
        done = int(doneP*100)
        if done > 100:
            done = 100
        # print("LoadingWindow.setProgress( " + str(done) + " )")
        self.text.set(str(done)+" % done" )
        return

    def killWindow(self):
        print("LoadingWindow.killWindow()")
        # self.settings['main']['settingsGeometry'] = self.geometry()
        self.destroy()








