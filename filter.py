import re
from time import *


class FilterReturnObject:
    colorText = "black"
    colorBg = "white"
    bold = False
    shouldShow = False


class Filter(object):
    """docstring for Filter"""

    enableFilter = False
    enableIgnore = False
    filtr = []
    ignore = []

    enableTime = False
    timeLow = 0
    timeHigh = 0
    timeLowStr = strptime("01.01.1950 01:01:01", "%d.%m.%Y %H:%M:%S")
    timeHighStr = strptime("01.01.2150 01:01:01", "%d.%m.%Y %H:%M:%S")

    enableErrors = True
    enableWarnings = True

    colorFilter = [[],[],[],[]]
    colorFilterColors = ['blue','green','gray','brown']

    errorColor = "black"
    errorColorBg = "red"
    warningColor = "black"
    warningColorBg = "orange"
    defaultColor = "black"
    defaultColorBg = "white"


    def __init__(self, settings, windowType):
        super(Filter, self).__init__()
        print ("Filter.__init__()")
        self.settings = settings
        self.windowType = windowType

        # loadLast = self.settings.getboolean(self.windowType, 'loadLastFilterSettings', fallback=False)
        # if loadLast:
        #     self.loadSettings("FilterCurrent"+self.windowType)
        # else:
        #     self.loadSettings("FilterDefault")
        # self.loadSettings()


    def loadSettings(self):
        settingsName = "FilterCurrent"+self.windowType
        if (settingsName in self.settings) == False:
            settingsName = "FilterDefault"

        enableFilter = self.settings.getboolean(settingsName,"enableFilter" , fallback=False)
        enableIgnore = self.settings.getboolean(settingsName,"enableIgnore" , fallback=False)
        filtr = self.getFiltersFromLine(self.settings.get(settingsName,"filtr" , fallback=""))
        ignore = self.getFiltersFromLine(self.settings.get(settingsName,"ignore" , fallback=""))

        enableTime = self.settings.getboolean(settingsName,"enableTime" , fallback=False)
        timeLow = self.settings.get(settingsName,"timeLow" , fallback=0)
        timeHigh = self.settings.get(settingsName,"timeHigh" , fallback=0)

        enableErrors = self.settings.getboolean(settingsName,"enableErrors" , fallback=True)
        enableWarnings = self.settings.getboolean(settingsName,"enableWarnings" , fallback=True)

        colorFilter = [
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter0", fallback="")),
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter1", fallback="")),
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter2", fallback="")),
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter3", fallback=""))]
        colorFilterColors = [
            self.settings.get(settingsName, "colorColor0", fallback="blue"),
            self.settings.get(settingsName, "colorColor1", fallback="green"),
            self.settings.get(settingsName, "colorColor2", fallback="gray"),
            self.settings.get(settingsName, "colorColor3", fallback="brown")]
        pass
        

    def testLine(self, inputItem):
        ret = FilterReturnObject()


        line = inputItem[2]
        if self.enableTime:
            #TODO time
            #if false, then return
            pass
        else:
            if self.enableFilter:
                for oneRegexp in self.filtr:
                    if re.search(oneRegexp, line):
                        ret.shouldShow = True
                        break
                
                #not found, check for divider
                if ret.shouldShow == False:
                    if line[0:2] == '----'[0:2]:
                        ret.shouldShow = True
            else:
                ret.shouldShow = True

            #coloring + force display ERRORS/WARNS
            if inputItem[3] == 'e':
                ret.ColorText = '#FF0000'
                ret.colorBg = "#FFbbbb"
                ret.bold = True
                if self.enableErrors:
                    ret.shouldShow = True
                    return ret
            else:
                if inputItem[3] == 'w':
                    ret.ColorText = '#dd8800'
                    ret.colorBg = "#FFbbbb"
                    ret.bold = True
                    if self.enableWarnings:
                        ret.shouldShow = True
                        return ret

            #there is no point in continue
            if ret.shouldShow == False:
                return ret

            #check ignore
            if self.enableIgnore:
                for oneRegexp in self.ignore:
                    if re.search(oneRegexp, line):
                        ret.shouldShow = False
                        return ret


            for i in range(4):
                for oneRegexp in self.colorFilter[i]:
                    if re.search(oneRegexp, line):
                        ret.colorText = colorFilterColors[i]
                        return ret

        return ret
                        

    #returns separated list of filters
    def getFiltersFromLine(self, text):
        ret = text.split(',')
        if ret[0] == '':
            if len(ret) == 1:
                ret = []
        if len(ret) > 1:
            if ret[-1] == '':
                ret = ret[0:-1]
        return ret
        
    #from separated list it creates list of 
    def getLineFromArray(self,array):
        ret = ''
        for item in array:
            ret = ret+item+','
        if ret != '':
            ret = ret[0:-1]
        return ret
        



