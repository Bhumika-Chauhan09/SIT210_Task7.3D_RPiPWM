#Libraries included
import RPi.GPIO as GPIO
import time
from time import sleep

#Raspberry Pi's pins initialised BOARD/BCM
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


#Set GPIO pins
LED = 40
GPIO_TRIGGER = 12
GPIO_ECHO = 18

#Setting Limit of distance after which the LED will not give any type of output
MAX_SET_DISTANCE = 20

#Initialised LED and TRIG to output and the ECHO for input as it catches signal outputted from trig
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Initialised LED pin to PWM mode 
led = GPIO.PWM(LED, 100)
led.start(0)

#For calculating the overall distance by calcultating the time taken by trigger pin's output to be recieved by echo
def Distance():
    #set trigger to High
    GPIO.output(GPIO_TRIGGER, True)
    #set trigger after  0.01ms to Low
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    while GPIO.input(GPIO_ECHO) == False:
        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == True:
        end_time = time.time()

    sig_time = end_time-start_time
    
    distance = sig_time / 0.000058
    return distance

try:
    while 1:
        dist = Distance()
        print(dis)
        if dis <= MAX_SET_DISTANCE:
            #Change the duty cycle as per the percentage calculated
            led.ChangeDutyCycle(100 - (dist/MAX_SET_DISTANCE * 100))
            time.sleep(0.1)
        else:
            led.ChangeDutyCycle(0)
            
except KeyboardInterrupt:
    print("Force Stopped")

#Reset the whole setup once exit
led.stop()
GPIO.cleanup()