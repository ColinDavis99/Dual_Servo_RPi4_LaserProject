#Example Servo Code

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 +2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)

count = 0
numLoops = 2

while count < numLoops:

        
    print("set to 75-deg")
    setAngle(180)
    sleep(1)
    
    count=count+1

pwm.stop()
GPIO.cleanup()
