#This is the code for the recciving tower on the mainland. This tower does not need to send so it recives data and it writes it to a text file.

import RFM69
from RFM69registers import *
import datetime
import time
import base64
cap = cv2.VideoCapture(0)
x=0


while true:
        rm = RFM69.RFM69(RF69_915MHZ, 1, 1, True)

        while True:
            rm.receiveBegin()
            while not test.receiveDone():
                time.sleep(.1)
            s = "%s from %s RSSI:%s" % (",".join([chr(letter) for letter in test.DATA]), test.SENDERID, test.RSSI)
                print s
                f = open('data.txt','w')
                f.write(s",")
                f.close()
            if rm.ACKRequested():

                rm.sendACK()
