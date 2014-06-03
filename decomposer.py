
import re


class Decomposer(object):
    """docstring for Decomposer"""
    defaultStrategy = "Ohm"
    selectedStrategy = defaultStrategy
    def __init__(self, settings, ohmterm):
        super(Decomposer, self).__init__()
        self.settings = settings
        self.settings = settings
        print ("Decomposer.__init__()")

        self.ohmStrategy = OhmStandard(ohmterm)

        self.strategies = {
        "None":decomposeStrategyNone,
         "PDM7":decomposeStrategyPDM7, 
         "Ohm": self.ohmStrategy.decomposeStrategyOhmStandard1 }

        self.setStrategy( self.settings.get('input', 'defaultDecomposer', fallback=self.defaultStrategy) )


    def decompose(self, rawData):
        data = []
        for line in rawData:
            try:
                data.append(self.strategy(line))
            except Exception as ex:
                print("ERROR decomposer")
                traceback.print_exc()
        return data

    def getAvailableStrategies(self):
        return self.strategies.keys()

    def addStrategy(self, name, func):
        self.strategies[name] = func;

    def getStrategy(self):
        return self.selectedStrategy

    def setStrategy(self, strategy):
        print ("Decomposer.setStrategy('"+strategy+"')")
        if strategy in self.strategies.keys():
            self.strategy = self.strategies[strategy]
            self.selectedStrategy = strategy
        else:
            print ("Decomposer.setStrategy ERROR: not found ('"+strategy+"')")
            self.setStrategy(self.defaultStrategy)
            return False
        
        self.settings['input']['defaultDecomposer'] = strategy
        return True






import datetime
import calendar
import time

#strategies for decomposing
def decomposeStrategyNone(text):
    return [0, "None", text, "d", "#000000", "#FFFFFF"]

def decomposeStrategyPDM7(text):
    return [0, "None", text, "d", "#000000", "#FFFFFF"]


class OhmStandard(object):
    """docstring for OhmStandard"""
    def __init__(self, ohmterm):
        super(OhmStandard, self).__init__()
        self.ohmterm = ohmterm
        
    def decomposeStrategyOhmStandard1(self, text):
        # print(text)
        splited = text.split()
        kind = "d"
        ColorText = "#000000"
        ColorBg = "#FFFFFF"

        if len(splited) < 3:
            return [0, "None", text, kind, ColorText, ColorBg]

        if len(splited[1])>0:
            if splited[1][0] == "E":
                kind = "e"
            elif splited[1][0] == "W":
                kind = "w"
            elif splited[1][0] == "X":
                if splited[2][0] == 'n': #empty line
                    self.ohmterm.allWindowsClear()

        if splited[2] == "OGRE":
            ColorText = "#222"
        # print(splited[2])

        timstamp = 0
        try:
            t = datetime.datetime.strptime("2014 "+splited[0]+"000","%Y %H:%M:%S.%f")
            # print (t.time().strftime("%H:%M:%S.%f"))
            timstamp = calendar.timegm(t.utctimetuple()) + t.microsecond  / 1000000.0
        except:
            print ("decomposeStrategyOhmStandard1() ERROR: time convert failed")
            pass

        return [timstamp, splited[2], text, kind, ColorText, ColorBg]