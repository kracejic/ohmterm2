import sys
try:
  from tkinter import *
except:
  try:
      from Tkinter import *
  except:
    print ("Tkinter lib is missing.")
    sys.exit()
  


import settings
import inputSerial
import filter





version1 = 2
version2 = 0
version3 = 0
betaFlag = True





root = Tk()


class OhmTerm(object):
  """docstring for OhmTerm"""
  datastore = []


  def __init__(self):
    super(OhmTerm, self).__init__()
    