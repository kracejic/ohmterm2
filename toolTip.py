try:
  from tkinter import *
except:
  try:
      from Tkinter import *
  except:
    print ("Tkinter lib is missing.")
    sys.exit()

from time import *

#-----------------------------------------------------------------------------------------------------------
# ToolTip class - I find this on internet
#-----------------------------------------------------------------------------------------------------------
class ToolTip( Toplevel ):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """ 
    def __init__( self, wdgt, msg=None, msgFunc=None, delay=1, follow=True ):
        """
        Initialize the ToolTip
        
        Arguments:
          wdgt: The widget this ToolTip is assigned to
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        self.parent = self.wdgt.master                                          # The parent of the ToolTip is the parent of the ToolTips widget
        Toplevel.__init__( self, self.parent, bg='black', padx=1, pady=1 )      # Initalise the Toplevel
        self.withdraw()                                                         # Hide initially
        self.overrideredirect( True )                                           # The ToolTip Toplevel should have no frame or title bar
        
        self.msgVar = StringVar()                                               # The msgVar will contain the text displayed by the ToolTip        
        if msg == None:                                                         
            self.msgVar.set( 'No message provided' )
        else:
            self.msgVar.set( msg )
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        #self.follow = False
        self.visible = 0
        self.lastMotion = 0
        Message( self, textvariable=self.msgVar, bg='#FFFFDD',
                 aspect=1000 ).grid()                                           # The test of the ToolTip is displayed in a Message widget
        self.wdgt.bind( '<Enter>', self.spawn, '+' )                            # Add bindings to the widget.  This will NOT override bindings that the widget already has
        self.wdgt.bind( '<Leave>', self.hide, '+' )
        self.wdgt.bind( '<Motion>', self.move, '+' )
        
    def spawn( self, event=None ):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget
        
        Arguments:
          event: The event that called this funciton
        """
        #print "a", self.msgVar.get(), "\n"
        self.visible = 1
        self.after( int( self.delay * 1000 ), self.show )                       # The after function takes a time argument in miliseconds
        #self.show() #ohnheiser hack
    def show( self ):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1:#ohnheiser hack and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()
            
    def move( self, event ):
        """
        Processes motion within the widget.
        
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        if self.follow == False:                                                # If the follow flag is not set, motion within the widget will make the ToolTip dissapear
            self.withdraw()
            self.visible = 1

        root = self.parent
           
        pa = re.split(r'(\D)', root.geometry())
        pt = re.split(r'(\D)', self.geometry())
        #pm = re.split(r'(\D)', self.master.geometry())
        #print "root:  ", pa
        #print "tool:  ", self.geometry()
        #print "pm:  ", self.wdgt.geometry()
        #print "mouse: ", event.x_root, event.y_root
        #print "mouser: ", event.x, event.y
        
        xCan = event.x_root - self.parent.winfo_rootx()
        yCan = event.y_root - self.parent.winfo_rooty()
        #print "mouser2: ", xCan, yCan
        
        
        
        #if pa[5] == '-':
        #  limit_x = int(pa[0]) - int(pa[6]) 
        #  print "minus"
        #else:
        #limit_x = int(pa[0]) + int(pa[4]) 
        #if root.state() == 'zoomed':
        limit_x = int(pa[0])
        #print "lim: ", limit_x
          
          
        if xCan > (limit_x-int(pt[0])):
          #print "xxx"
          self.geometry( '+%i+%i' % ( event.x_root-int(pt[0]), event.y_root+10 ) )        # Offset the ToolTip 10x10 pixes southwest of the pointer
        else:
          self.geometry( '+%i+%i' % ( event.x_root+10, event.y_root+10 ) )        # Offset the ToolTip 10x10 pixes southwest of the pointer
        try:
            self.msgVar.set( self.msgFunc() )                                   # Try to call the message function.  Will not change the message if the message function is None or the message function fails
        except:
            pass
        self.after( int( self.delay * 1000 ), self.show )
        
        
        
            
    def hide( self, event=None ):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()