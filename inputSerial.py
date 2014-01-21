import sys
try:
  from tkinter import *
except:
  try:
      from Tkinter import *
  except:
    print ("Tkinter lib is missing.")
    sys.exit()


import genericinput


# 21.02.2012 16:12:15.984 009907 MenuProc        DEBUG: ** evMenuProcConfirmCmd (scheduled)
# 21.02.2012 16:12:15.994 009908 MenuProc        DEBUG: << evMenuProcConfirmCmd (consumed)
# 21.02.2012 16:12:16.005 009909 MenuProc        DEBUG: -MenuOpened: Selection -> Confirm
# 21.02.2012 16:12:16.909 009916 MenuProc        DEBUG: ** evMenuProcExecuteCmd (scheduled)
# 21.02.2012 16:12:16.919 009917 MenuProc        DEBUG: << evMenuProcExecuteCmd (consumed)

class InputSerial(genericinput.Input):
  """docstring for InputSerial"""
  connected = False;
  def __init__(self):
    super(InputSerial, self).__init__()


  def open(self, adress):
    try:
      self.ser = serial.Serial(int(adress), 115200, timeout=0.02, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)  # open first serial port
    except:
      return False
    # check which port was really used
    print ("Trying to connect to: ", port, ". Portstr: ", self.ser.portstr)       
    self.connected = True
    return True
  

  def close(self):
    self.ser.close()
    self.connected = 0  

  def getStatus(self):
    return self.connected
  

  def getData(self):
    output = []
    if self.Status() == False:
      return []


    for z in range(800):
      try:
        line = self.ser.readline()   # read a '\n' terminated line
        if line != "":
          if ord(line[0]) != 13:
            #print ("1line:"+  line)
            #print ("ord: ", ord(line[-2]))
            if len(line) >= 2:
              if ord(line[-2]) == 13:
                line = line[0:-2]
            #print ("2line:"+  line)
            if line[0:4] == 'DBG:':
              line = line[4:]  
            output.append(line)
        else:
          if z > 780:
            self.toomuchdata = 1
          else:
            self.toomuchdata = 0
          return output

      except:
        print ("------------------------------------------------------------")
        print ("ERROR: Comport reading error :(")
        traceback.print_exc(file=sys.stdout)      

    self.toomuchdata = 1
    return output    