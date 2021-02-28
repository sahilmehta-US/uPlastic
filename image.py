import os

def get_image():
    os.system("fswebcam --no-banner sampleImage.jpg")

def archive_image():
    os.System("mv sampleImage.jpg archive/")
    
