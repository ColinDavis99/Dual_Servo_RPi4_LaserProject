# Example Servo Code

import RPi.GPIO as GPIO
from pygame import key
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm = GPIO.PWM(11, 50)
pwm.start(0)

def set_angle_return(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)
    return angle;

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(.15)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)

def init_x_pos():
    duty = 30 / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)


def movement(st_angle):
    flag = True
    while flag:
        value = int(input("Please enter a direction:\n"))
        if value == 0:
            init_x_pos()
            flag = False
            print("Turn over")

        elif value == 1: # left function
            while (st_angle <= 60):
                st_angle += 3
                set_angle(st_angle)
        elif value == 2: # right function
            while (st_angle >= 5):
                st_angle -= 3
                set_angle(st_angle)

        

init_x_pos()
sleep(1)      
movement(st_angle = 30)
pwm.stop()
GPIO.cleanup()
