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
        self.loadSettings()


    def loadSettings(self):
        settingsName = "FilterCurrent"+self.windowType
        if (settingsName in self.settings) == False:
            settingsName = "FilterDefault"

        self.enableFilter = self.settings.getboolean(settingsName,"enablefilter" , fallback=False)
        # if self.enableFilter == '0':
        #     self.enableFilter = False
        # else:
        #     self.enableFilter = True

        self.enableIgnore = self.settings.getboolean(settingsName,"enableignore" , fallback=False)
        # if self.enableIgnore == '0':
        #     self.enableIgnore = False
        # else:
        #     self.enableIgnore = True
        self.filtrLine = self.settings.get(settingsName,"filtr" , fallback="")
        self.filtr = self.getFiltersFromLine(self.settings.get(settingsName,"filtr" , fallback=""))
        self.ignoreLine = self.settings.get(settingsName,"ignore" , fallback="")
        self.ignore = self.getFiltersFromLine(self.settings.get(settingsName,"ignore" , fallback=""))

        self.enableTime = self.settings.getboolean(settingsName,"enableTime" , fallback=False)
        self.timeLow = self.settings.get(settingsName,"timeLow" , fallback=0)
        self.timeHigh = self.settings.get(settingsName,"timeHigh" , fallback=0)

        self.enableErrors = self.settings.getboolean(settingsName,"enableErrors" , fallback=True)
        self.enableWarnings = self.settings.getboolean(settingsName,"enableWarnings" , fallback=True)

        self.colorFilter = [
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter0", fallback="")),
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter1", fallback="")),
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter2", fallback="")),
            self.getFiltersFromLine(self.settings.get(settingsName, "colorFilter3", fallback=""))]
        self.colorFilterColors = [
            self.settings.get(settingsName, "colorColor0", fallback="blue"),
            self.settings.get(settingsName, "colorColor1", fallback="green"),
            self.settings.get(settingsName, "colorColor2", fallback="gray"),
            self.settings.get(settingsName, "colorColor3", fallback="brown")]
        pass
        
    # inputItem[0] - time
    # inputItem[1] - component
    # inputItem[2] - string
    # inputItem[3] - type
    def testLine(self, inputItem):
        ret = FilterReturnObject()
        # print (str(self.enableFilter) + " - FILTRY = " + str(self.filtr))
        # print (str(self.enableIgnore) + " - IGNORE = " + str(self.ignore))
        ret.colorText = inputItem[4]
        ret.colorBg = inputItem[5]

        line = inputItem[2]
        # print ("LINE: " + inputItem[2])
        if self.enableTime:
            #TODO time
            #if false, then return
            pass
        else:
            if self.enableFilter:
                for oneRegexp in self.filtr:
                    if re.search(oneRegexp, line, re.IGNORECASE):
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
                ret.colorText = '#FF0000'
                ret.colorBg = "#FFbbbb"
                ret.bold = True
                if self.enableErrors:
                    ret.shouldShow = True
                    return ret
            else:
                if inputItem[3] == 'w':
                    ret.colorText = '#dd8800'
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
                    if re.search(oneRegexp, line, re.IGNORECASE):
                        ret.shouldShow = False
                        return ret


            for i in range(4):
                for oneRegexp in self.colorFilter[i]:
                    if re.search(oneRegexp, line, re.IGNORECASE):
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
        



