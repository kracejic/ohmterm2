


class Input(object):
    """docstring for Input"""
    kind = "none"
    connected = False

    def __init__(self, settings):
        super(Input, self).__init__()
        print("Input init, kind=" + self.kind)
        self.settings = settings


    def open(self, address):
        self.settings[self.kind]['address'] = address
        self.connected = True
        return self.connected

    def close(self):
        self.connected = False
        pass

    def getStatus(self):
        return self.connected
        
    def getData(self):
        data = []
        return data

    def getAddress(self):
        return self.settings.get(self.kind, 'address', fallback="0")

        