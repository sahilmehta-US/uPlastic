import RPi.GPIO as GPIO

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

def filter_rotate(dsec):
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    try:
        p.ChangeDutyCycle(5)
        time.sleep(dsec)
        p.ChangeDutyCycle(7.5)
        time.sleep(dsec)
        p.ChangeDutyCycle(10)
        time.sleep(dsec)
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()
