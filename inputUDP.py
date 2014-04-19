import sys
import genericinput
import socket
import traceback

class InputUDP(genericinput.Input):
    """docstring for InputUDP"""
    connected = False;
    kind = "udp"

    UDP_IP = "127.0.0.1"
    UDP_PORT = 55009

    def __init__(self, settings):
        super(InputUDP, self).__init__(settings)

    
    def open(self, address):
        self.settings[self.kind]['address'] = address
        print("InputUDP.open()")

        try:
            port = int(address)
            self.UDP_PORT = port

            self.sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
            self.sock.bind((self.UDP_IP, self.UDP_PORT))
            self.sock.setblocking(0)
            
            print("InputUDP - connected to " + str(self.UDP_IP) + ":" + str(self.UDP_PORT))
        except:
            self.connected = False
            print ("ERROR: InputUDP - opening socket FAILED")
            traceback.print_exc(file=sys.stdout)

        self.connected = True
        return True

    
    def close(self):
        print("InputUDP.close()")
        if self.connected == False:
            return
        try:
            self.sock.close()
        except:
            print ("ERROR: InputUDP - closing socket FAILED")
            traceback.print_exc(file=sys.stdout)
        self.connected = False
        pass

    
    def getStatus(self):
        return self.connected
        

    def getData(self):
        if self.connected == False:
            return []
        data = []
        try:
            x = 0
            while x < 100: 
                x = x + 1
                ddd, addr = self.sock.recvfrom(8192)
                dd = ddd.decode('unicode_escape')
                data = data + dd.split("\n")
        except BlockingIOError as e:
            pass
        except:
            print ("ERROR: InputUDP.getData - failed")
            traceback.print_exc(file=sys.stdout)
            self.close()

        return data
        

# import socket

# UDP_IP = "127.0.0.1"
# UDP_PORT = 55009

# sock = socket.socket(socket.AF_INET, # Internet
#                  socket.SOCK_DGRAM) # UDP
# sock.bind((UDP_IP, UDP_PORT))

# while True:
#     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#     print data    
#data:
#23:06:34.528 INFO  MAIN : -----------------------------------------------
#23:06:34.529 INFO  MAIN :         Log component stopped
#23:06:34.529 INFO  MAIN : -----------------------------------------------


