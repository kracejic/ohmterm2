import sys

import genericinput
import inputTester
import inputSerial
import inputUDP



class InputStrategy(object):
    """docstring for InputStrategy"""
    connected = False;
    defaultInput = 'test'
    def __init__(self, settings):
        super(InputStrategy, self).__init__()
        print ("InputStrategy.__init__()")
        self.settings = settings
        self.inputer = genericinput.Input(settings)


        self.switchInput( self.settings.get('input', 'defaultMethod', fallback=self.defaultInput) )
        if self.settings.getboolean('input', 'autoconnect', fallback=False):
            self.open(self.getAddress())

    def getInputs(self):
        return ["test","udp","com"]

        
    def switchInput(self, onWhat):
        print ("InputStrategy.switchInput("+onWhat+")")
        self.inputer.close()

        if onWhat == "test":
            self.inputer = inputTester.InputTester(self.settings);
        elif onWhat == "none":
            self.inputer = genericinput.Input(self.settings);
        elif onWhat == "udp":
            self.inputer = inputUDP.InputUDP(self.settings);
        elif onWhat == "com":
            self.inputer = inputSerial.InputSerial(self.settings);

    def getAddress(self):
        return self.inputer.getAddress();

    def open(self, address):
        return self.inputer.open(address)

    def close(self):
        return self.inputer.close()

    def getStatus(self):
        return self.inputer.getStatus()
        
    def getData(self):
        return self.inputer.getData()

    def getKind(self):
        return self.inputer.kind

