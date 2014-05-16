import wx
#import serial

POS_WIDTH_A = 100
POS_HEIGHT_A = 100
SIZE_WIDTH_A = 200
SIZE_HEIGHT_A = 100

POS_WIDTH_B = 300
POS_HEIGHT_B = 100
SIZE_WIDTH_B = 200
SIZE_HEIGHT_B = 100

'''
movespeed = 20 #Rate at which signals are sent milli secs

ser = serial.Serial()

def openserialPort(port, baudr):
    try:
        ser.baudrate = baudr
        ser.port = port
        ser.open()
        print "Serial port Open"
    except serial.SerialException:
        print "Serial port not avaiable"
        return 0
    return 1



def writetoSerial(num):
    if(ser.isOpen()):
        print "Writing to port"
        ser.write(num)
    else:
        print "No Go"
'''

class RoboticArmFrameGUI(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(600, 650))
        panel = wx.Panel(self)

        panel.SetBackgroundColour('Black')

        statusBar = self.CreateStatusBar()
        
        buttonA0 = wx.ToggleButton(panel, id = 6, label="Close Claw", pos=(POS_WIDTH_A, POS_HEIGHT_A - 50 + POS_HEIGHT_A*0), size=(SIZE_WIDTH_A, SIZE_HEIGHT_A))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickA0, buttonA0)

        buttonA1 = wx.ToggleButton(panel, id = 5 , label="Rotate Claw Left", pos=(POS_WIDTH_A, POS_HEIGHT_A - 50 + POS_HEIGHT_A*1), size=(SIZE_WIDTH_A, SIZE_HEIGHT_A))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickA1, buttonA1)

        buttonA2 = wx.ToggleButton(panel, id = 2, label="Elbow Forward", pos=(POS_WIDTH_A, POS_HEIGHT_A - 50 + POS_HEIGHT_A*2), size=(SIZE_WIDTH_A, SIZE_HEIGHT_A))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickA2, buttonA2)

        buttonA3 = wx.ToggleButton(panel, id = 0, label="Arm Right", pos=(POS_WIDTH_A, POS_HEIGHT_A - 50 + POS_HEIGHT_A*3), size=(SIZE_WIDTH_A, SIZE_HEIGHT_A))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickA3, buttonA3)

        buttonA4 = wx.ToggleButton(panel, id = 9, label="Arm Up", pos=(POS_WIDTH_A, POS_HEIGHT_A - 50 + POS_HEIGHT_A*4), size=(SIZE_WIDTH_A, SIZE_HEIGHT_A))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickA4, buttonA4)

        buttonB0 = wx.ToggleButton(panel, id = 7, label="Open Claw", pos=(POS_WIDTH_B, POS_HEIGHT_B - 50 + POS_HEIGHT_B*0), size=(SIZE_WIDTH_B, SIZE_HEIGHT_B))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickB0, buttonB0)

        buttonB1 = wx.ToggleButton(panel, id = 4, label="Rotate Claw Right", pos=(POS_WIDTH_B, POS_HEIGHT_B - 50 + POS_HEIGHT_B*1), size=(SIZE_WIDTH_B, SIZE_HEIGHT_B))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickB1, buttonB1)
        
        buttonB2 = wx.ToggleButton(panel, id = 3, label="Elbow Backward", pos=(POS_WIDTH_B, POS_HEIGHT_B - 50 + POS_HEIGHT_B*2), size=(SIZE_WIDTH_B, SIZE_HEIGHT_B))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickB2, buttonB2)
        
        buttonB3 = wx.ToggleButton(panel, id = 1, label="Arm Left", pos=(POS_WIDTH_B, POS_HEIGHT_B - 50 + POS_HEIGHT_B*3), size=(SIZE_WIDTH_B, SIZE_HEIGHT_B))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickB3, buttonB3)
        
        buttonB4 = wx.ToggleButton(panel, id = 8, label="Arm Down", pos=(POS_WIDTH_B, POS_HEIGHT_B - 50 + POS_HEIGHT_B*4), size=(SIZE_WIDTH_B, SIZE_HEIGHT_B))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleClickB4, buttonB4)

        self.timer1 = wx.Timer(self, id = 30)
        self.timer2 = wx.Timer(self, id = 40)
        self.timer3 = wx.Timer(self, id = 50)
        self.timer4 = wx.Timer(self, id = 60)
        self.timer5 = wx.Timer(self, id = 70)
        

        return

    def OnTimerStart(self, event, num):
        label = event.GetId()
        print label
        writetoSerial(num)

    def OnToggleClickA0(self, event):
        isPressed = event.GetEventObject().GetValue()

        if isPressed:
           print "A0 is clicked"
           self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "6"), self.timer1)
           self.timer1.Start(movespeed)
        elif not isPressed:
            print "A0 is un-clicked" 
            self.timer1.Stop()
            self.timer1.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickB0(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            print "B0 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "7"), self.timer1)
            self.timer1.Start(movespeed)
        elif not isPressed:
            print "B0 is un-clicked"
            self.timer1.Stop()
            self.timer1.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickA1(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "5"), self.timer2)
            self.timer2.Start(movespeed*3)
            print "A1 is clicked"
        elif not isPressed:
            print "A1 is un-clicked"
            self.timer2.Stop()
            self.timer2.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickB1(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            print "B1 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "4"), self.timer2)
            self.timer2.Start(movespeed*3)
        elif not isPressed:
            print "B1 is un-clicked"
            self.timer2.Stop()
            self.timer2.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickA2(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            print "A2 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "2"), self.timer3)
            self.timer3.Start(movespeed*2)
        elif not isPressed:
            print "A2 is un-clicked"
            self.timer3.Stop()
            self.timer3.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickB2(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            print "B2 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "3"), self.timer3)
            self.timer3.Start(movespeed*2)
        elif not isPressed:
            print "B2 is un-clicked"
            self.timer3.Stop()
            self.timer3.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickA3(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            print "A3 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "0"), self.timer4)
            self.timer4.Start(movespeed*4)
        elif not isPressed:
            print "A3 is un-clicked"
            self.timer4.Stop()
            self.timer4.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickB3(self, event):
        isPressed = event.GetEventObject().GetValue()
        if isPressed:
            print "B3 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "1"), self.timer4)
            self.timer4.Start(movespeed*4)
        elif not isPressed:
            print "B3 is un-clicked"
            self.timer4.Stop()
            self.timer4.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickA4(self, event):
        isPressed = event.GetEventObject().GetValue()
        print isPressed
        if isPressed:
            print "A4 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "9"), self.timer5)
            self.timer5.Start(movespeed*1.8)
        elif not isPressed:
            print "A4 is un-clicked"
            self.timer5.Stop()
            self.timer5.Unbind(wx.EVT_TIMER)
        return

    def OnToggleClickB4(self, event):
        isPressed = event.GetEventObject().GetValue()
        print isPressed
        if isPressed:
            print "B4 is clicked"
            self.Bind(wx.EVT_TIMER, lambda evt : self.OnTimerStart(evt, "8"), self.timer5)
            self.timer5.Start(movespeed*1.8)
        elif not isPressed:
            print "B4 is un-clicked"
            self.timer5.Stop()
            self.timer5.Unbind(wx.EVT_TIMER)
        return

if __name__ == '__main__':
#    if(openserialPort(3,38400)):
        app = wx.PySimpleApp()
        frame = RoboticArmFrameGUI(parent=None, id=-1)
        frame.Show()
        app.MainLoop()
