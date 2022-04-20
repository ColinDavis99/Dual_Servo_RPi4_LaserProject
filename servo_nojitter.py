# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 1 second")
time.sleep(1)


def setAngle(angle):
    duty = angle / 18 +2
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(duty)
    GPIO.output(11, False)
    servo1.ChangeDutyCycle(duty)

# Define variable duty
duty = 0

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 6:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.05)
    duty = duty + .15

# Wait a couple of seconds
time.sleep(1)

while duty >= 0:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.05)
    duty = duty - .15
#turn back to 0 degrees
print ("Turning back to 0 degrees")
setAngle(-12)
time.sleep(0.5)


servo1.stop()
GPIO.cleanup()
