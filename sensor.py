from image import get_image
from mlearn import keras_detect

results = open("result.txt", "a")

def sensor_run():
    get_image()
    filter_rotate()
    prediction = keras_detect()
    results.write(prediction)
    sleep(interval)

if __name__ == "__main__":
    sensor_run()
    results.close()
    
