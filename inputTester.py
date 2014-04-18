import sys
import genericinput
import random
import datetime



class InputTester(genericinput.Input):
    """docstring for InputTester"""
    connected = False;
    kind = "test"

    kinds = ["INFO ", "DEBUG", "ERROR", "WARN "]
    components = ["MAIN   ", "DISPLAY", "COMPROC"]
    messages = ["component started", "component stopped", "Log text", \
    "something went well", "something does not work", "success", "fail", \
    "HACA CHYBA 1", "HACA CHYBA random access", "memory"]

    def __init__(self, settings):
        super(InputTester, self).__init__(settings)

    def open(self, address):
        self.settings[self.kind]['address'] = address
        self.connected = True
        return True

    def close(self):
        self.connected = False
        pass

    def getStatus(self):
        return self.connected
        
    def getData(self):
        #if not connected, go away
        if self.connected == False:
            return []

        data = []

        kind = "INFO "
        if random.random() > 0.95:
            kind = "WARN "
            if random.random() > 0.6:
                kind = "ERROR"

        if random.random() > 0.6:
            txt = datetime.datetime.now().time().strftime("%H:%M:%S.%f")
            txt = txt[:12]

            txt = txt + " " + kind
            txt = txt + " " + random.choice(self.components)
            txt = txt + " " + random.choice(self.messages)

            data.append(txt)

        return data
        

        #data:
        #23:06:34.528 INFO  MAIN : -----------------------------------------------
        #23:06:34.529 INFO  MAIN :         Log component stopped
        #23:06:34.529 INFO  MAIN : -----------------------------------------------
        