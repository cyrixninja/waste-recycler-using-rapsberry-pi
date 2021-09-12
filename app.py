import ml
import RPi.GPIO as GPIO # Import Library to access GPIO PIN
import capture
import time # To access delay function
import mysql.connector
from mysql.connector.constants import ClientFlag
import datetime
from gpiozero import Servo
from time import sleep

servo = Servo(12)
servo1 =Servo(13)
servo2 =Servo(16)
now = datetime.datetime.now()
date=(now.strftime('"%Y-%m-%d"'))

config = {
    'user': 'root',
    'password': 'admin666',
    'host': '34.71.98.84',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}

config['database'] = 'pythondb'
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()


GPIO.setmode(GPIO.BCM) # Consider complete raspberry-pi board

GPIO.setwarnings(False) # To avoid same PIN use warning

TRIG = 17 # Define PIN for Trigger pin
ECHO = 4  # Define PIN for Echo pin
ELECTRONIC_LED_PIN = 18 # Define PIN for LED
ORGANIC_LED_PIN = 23
RECYCLABLE_LED_PIN = 24

GPIO.setup(ELECTRONIC_LED_PIN,GPIO.OUT) # Set pin function as output
GPIO.setup(ORGANIC_LED_PIN ,GPIO.OUT)
GPIO.setup(RECYCLABLE_LED_PIN,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN) # Set pin function input as

GPIO.setup(TRIG,GPIO.OUT) # Set pin function as output

GPIO.output(TRIG, False)


print("Waiting For Sensor To Settle")

time.sleep(1)

while (True): # To start transmit the sound from ultrasonic sensor

   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)

   while GPIO.input(ECHO)==0:

     pulse_start = time.time()

   while GPIO.input(ECHO)==1:

     pulse_end = time.time()
     pulse_duration = pulse_end - pulse_start
 
     distance = pulse_duration * 17150
     distance = round(distance, 2)
     print("Distance between obstacle and object is " + str(distance))
     if(distance > 50):
         print("not in range")

     else:
        capture.capturepic()
        if ml.electronics >= 0.6:
            query = f"INSERT INTO wastedata (date, wastetype) VALUES ({date}, 'Electronic')"
            cursor.execute(query)
            cnxn.commit()
            GPIO.output(ELECTRONIC_LED_PIN,GPIO.HIGH)
            print("Electronic Waste")
            while True:
                servo.min()
                sleep(20)
                servo.max()
        elif ml.organic >=0.6:
            query = f"INSERT INTO wastedata (date, wastetype) VALUES ({date}, 'Organic')"
            cursor.execute(query)
            cnxn.commit()
            print("Organic Waste")
            GPIO.output(ELECTRONIC_LED_PIN,GPIO.HIGH)
            while True:
                servo.min()
                sleep(20)
                servo.max()
        elif ml.recyclable >=0.6:
            query = f"INSERT INTO wastedata (date, wastetype) VALUES ({date}, 'Recyclable')"
            cursor.execute(query)
            cnxn.commit()
            print("Recyclable Waste")
            GPIO.output(RECYCLABLE_LED_PIN,GPIO.HIGH)
            while True:
                servo.min()
                sleep(20)
                servo.max()