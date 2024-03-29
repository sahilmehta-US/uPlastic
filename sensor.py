import time
import argparse
import numpy as np
from image import get_image
from image import archive_image
from mlearn import keras_detect
from mlearn import get_labels
from filter import filter_rotate

parser = argparse.ArgumentParser()
parser.add_argument("--interval", help="Timer interval", type=int, default=180)
parser.add_argument("--delay", help="Delay interval", type=int, default=2)
parser.add_argument("--rotate", help="Filter rotate", action='store_true')
args = parser.parse_args()

isec = args.interval
dsec = args.delay

results = open("result.txt", "a")

def sensor_run():
    imageName = "sampleImage.jpg"
    labels = get_labels("model/labels.txt")
    try:
        while True:
            get_image(imageName)
            prediction = keras_detect(imageName)
            print(prediction)
            index = np.argmax(prediction)
            score = prediction[0][index]
            label = labels[index]
            id = "{0} {1}\n".format(score*100, label)
            results.write(id)
            filter_rotate(dsec)
            archive_image()
            time.sleep(isec)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    if args.rotate:
        filter_rotate(dsec)
        exit(0)
    sensor_run()
    results.close()
    
