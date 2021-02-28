import time
import argparse
from image import get_image
from image import archive_image
from mlearn import keras_detect

parser = argparse.ArgumentParser()
parser.add_argument("--interval", help="Timer interval", type=int, default=180)
parser.add_argument("--delay", help="Delay interval", type=int, default=1)
parser.add_argument("--cycle", help="Duty cycle", type=int, default=1)
args = parser.parse_args()

isec = args.interval
dsec = args.delay
cycle = args.cycle

if cycle <=0 or cycle >=99:
   print("Duty Cycle %d is outside range 0-100" % cycle)
   exit(0)

results = open("result.txt", "a")

def sensor_run():
    imageName = "sampleImage.jpg"
    try:
        while True:
            get_image(imageName)
            prediction = keras_detect(imageName)
            #results.write(prediction)
            print(prediction)
            #filter_rotate()
            archive_image()
            time.sleep(isec)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    sensor_run()
    results.close()
    
