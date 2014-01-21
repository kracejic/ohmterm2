import sys
import genericinput


class InputTester(genericinput.Input):
  """docstring for InputTester"""
  connected = False;
  def __init__(self):
    super(InputTester, self).__init__()

  def open(self, adress):
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





    return data
    

    #data:
    #23:06:34.528 INFO  MAIN : -----------------------------------------------
    #23:06:34.529 INFO  MAIN :         Log component stopped
    #23:06:34.529 INFO  MAIN : -----------------------------------------------
    