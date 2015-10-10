import RPi.GPIO as GPIO
import time
import requests

#Initialize the GPIOs
GPIO.setmode(GPIO.BCM) #This is to name GPIOS
GPIO.setwarnings(False)
p1 = 17
p2 = 27
#Initialize the pins to their INPUT/OUPUT nature
#GPIO.setup(pinNumber,GPIO.IN/OUT)
GPIO.setup(p1,GPIO.OUT)
GPIO.setup(p2,GPIO.OUT)

'''This part is working with  the cloud'''
''' This is the voice input converted to text coming from the cloud '''
link = "https://still-tundra-5719.herokuapp.com/robot"
def checkCommandExists():
        r = requests.get(link)
        curValue = r.text
        if curValue == "0":
                return "0"
        else:
                return curValue

def getSerialCommand(cmd):
        if "go" in cmd and "forward" in cmd:
                print "f"
                moveForward()
        elif "go" in cmd and "back" in cmd:
                print "b"
                moveBackward()
        elif "go" in cmd and "right" in cmd:
                print "r"
                moveRight()
        elif "go" in cmd and "left" in cmd:
                print "l"
                moveLeft()
        elif "stop" in cmd or "wait" in cmd or "halt" in cmd:
                print "s"
                stop()
'''This part here is to work with your application, this case it is a wheelchair '''
def moveForward():
        GPIO.output(p1,GPIO.HIGH)#Both the pins will be high, moving forward
        GPIO.output(p2,GPIO.HIGH)
        print "forward"
def moveForward():
        GPIO.output(p1,GPIO.HIGH)#Both the pins will be high, moving forward
        GPIO.output(p2,GPIO.HIGH)
        print "forward"
def stop():
        GPIO.output(p1,GPIO.LOW)#Both wheels come to halt
        GPIO.output(p1,GPIO.LOW)
        print "stop"
def moveRight():
        GPIO.output(p1,GPIO.HIGH)#One moves, other doesn't
        time.sleep(0.5)
        GPIO.output(p2,GPIO.LOW)
        print "Right"
def moveLeft():
        GPIO.output(p2,GPIO.HIGH)#same logic as above
        time.sleep(0.5)
        GPIO.output(p1,GPIO.LOW)
        print "Left"
def moveBackward():
        GPIO.output(p1,GPIO.HIGH)#move in the same direction and 180degree turn


'''Run this infinitely'''
while True:
        val = checkCommandExists()
        if val != "0":
                val = getSerialCommand(val)

