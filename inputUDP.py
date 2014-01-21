import sys
import genericinput


class InputUDP(genericinput.Input):
  """docstring for InputUDP"""
  connected = False;
  def __init__(self):
    super(InputUDP, self).__init__()

  def open(self, adress):
    return False

  def close(self):
    self.connected = False
    pass

  def getStatus(self):
    return False
    
  def getData(self):
    #if not connected, go away
    if self.connected == False:
      return []
    data = []



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


