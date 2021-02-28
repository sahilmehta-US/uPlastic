import os
import datetime

def get_image():
    os.system("fswebcam --no-banner sampleImage.jpg")

def archive_image():
    currentTime = datetime.datetime.now()
    currentStr = currentTime.strftime("%Y%m%d_%H%M%S")
    sampleFilename = "sample_%s" % currentStr
    cmd = "mv sampleImage.jpg archive/%s" % sampleFilename
    os.system(cmd)
    
