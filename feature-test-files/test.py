from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
servo = Servo(27)

while True:
    servo.min()
    GPIO.output(17,GPIO.LOW)
    sleep(10)
    servo.max()
    GPIO.output(17,GPIO.HIGH)

