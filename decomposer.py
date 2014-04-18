
import re


class Decomposer(object):
    """docstring for Decomposer"""
    defaultStrategy = "Ohm"
    selectedStrategy = defaultStrategy
    def __init__(self, settings):
        super(Decomposer, self).__init__()
        self.settings = settings
        print ("Decomposer.__init__()")

        self.setStrategy( self.settings.get('input', 'defaultDecomposer', fallback=self.defaultStrategy) )

    def decompose(self, rawData):
        data = []
        for line in rawData:
            data.append(self.strategy(line))
        return data

    def getAvailableStrategies(self):
        return ["None", "PDM7", "Ohm"]

    def getStrategy(self):
        return self.selectedStrategy

    def setStrategy(self, strategy):
        print ("Decomposer.setStrategy('"+strategy+"')")
        if strategy == "None":
            self.strategy = decomposeStrategyNone
        elif strategy == "PDM7":
            self.strategy = decomposeStrategyPDM7
        elif strategy == "Ohm":
            self.strategy = decomposeStrategyOhmStandard1
        else:
            print ("Decomposer.setStrategy ERROR: not found ('"+strategy+"')")
            self.setStrategy(self.defaultStrategy)
            return False
        
        self.settings['input']['defaultDecomposer'] = strategy
        self.selectedStrategy = strategy
        return True






import datetime
import calendar
import time

#strategies for decomposing
def decomposeStrategyNone(text):
    return [0, "None", text, "d"]

def decomposeStrategyPDM7(text):
    return [0, "None", text, "d"]

def decomposeStrategyOhmStandard1(text):
    splited = text.split()
    kind = "d"
    if splited[1][0] == "E":
        kind = "e"
    elif splited[1][0] == "W":
        kind = "w"

    timstamp = 0
    try:
        t = datetime.datetime.strptime("2014 "+splited[0]+"000","%Y %H:%M:%S.%f")
        # print (t.time().strftime("%H:%M:%S.%f"))
        timstamp = calendar.timegm(t.utctimetuple()) + t.microsecond  / 1000000.0
    except:
        print ("decomposeStrategyOhmStandard1() ERROR: time convert failed")
        pass

    return [timstamp, splited[2], text, kind]