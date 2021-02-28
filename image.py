import os
import datetime

def get_image():
    os.system("fswebcam --no-banner sampleImage.jpg")

def archive_image():
    current = datetime.datetime()
    filename = "sample_%s" % current
    cmd = "mv sampleImage.jpg archive/%s" % filename
    os.System(cmd)
    
