'''lines 4-5 import the RPi.GPIO module and set up the BCM port numbering scheme

line 8 sets GPIO 23 as an input with the pullup resistor set to UP.
This means that the signal will be HIGH all the time until the button is pressed connecting the port to GND, which makes it LOW. This avoids false event detection.

lines 10-11 print some instructions
line 12 waits for user to hit enter before starting. This gives an opportunity to check the wiring

lines 14-21 further instructions and documentation

line 22 try: & line 26 except KeyboardInterrupt:
This allows us to run the program and exit cleanly if someone presses CTRL-C to stop the program. If we didn’t do this, the ports would still be set when we forcefully exit the program.

line 23 sets up the “wait for the signal on port 23 to start falling towards 0″

lines 24-25 further on-screen instructions

line 27 cleans up the GPIO ports we’ve used during this program when CTRL-C is pressed
line 28 cleans up the GPIO ports we’ve used during this program when the program exits normally '''
#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Make sure you have a button connected so that when pressed"
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
raw_input("Press Enter when ready\n>")

print "Waiting for falling edge on port 23"
# now the program will do nothing until the signal on port 23 
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt

print "During this waiting time, your computer is not" 
print "wasting resources by polling for a button press.\n"
print "Press your button when ready to initiate a falling edge interrupt."
try:
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print "\nFalling edge detected. Now your program can continue with"
    print "whatever was waiting for a button press."
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit

