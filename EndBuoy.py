#This is the code for the last buoy in the mesh network. Scince it cannot recive, anything, it only sends data to the other nodes.


import RFM69
from RFM69registers import *
import datetime
import time
import base64
cap = cv2.VideoCapture(0)
x=0

def picturetakeandsend:
        import cv2
        camera_port = 1
        ramp_frames = 30
        camera = cv2.VideoCapture(camera_port)

        def get_image():

         retval, im = camera.read()
         return im

        for i in xrange(ramp_frames):
         temp = get_image()
        print("Taking image...")

        camera_capture = get_image()
        file = "/home/Desktop/datapics/"x+1

        cv2.imwrite(file, camera_capture)

        del(camera)

        with open("/home/Desktop/datapics"x+1, "rb") as imageFile:
            base64e = base64.b64encode(imageFile.read())
            print base64e
        x+1

        rm = RFM69.RFM69(RF69_915MHZ, 1, 1, True)
        print "class initialized"
        print "reading all registers"
        results = rm.readAllRegs()
        for result in results:
            print result
        print "Performing rcCalibration"
        rm.rcCalibration()
        print "setting high power"
        rm.setHighPower(True)
        print "Checking temperature"
        print picture.take
        print "setting encryption"
        rm.encrypt("1234567891011121")
        print "sending blah to 2"
        if rm.sendWithRetry(2, base64e);
            print "ack recieved"



while true:

    picturetakeandsend
    time.sleep(10000)
