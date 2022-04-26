#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time
import RPi.GPIO as GPIO
from time import sleep

# Gamepad settings
gamepadType = Gamepad.PS4
buttonTrigger = 'CROSS'
buttonLeft = 'CIRCLE'
buttonExit = 'L2'
buttonRight = 'L1'
buttonDown = 'TRIANGLE'
buttonUp = 'SQUARE'
# Servo Settings 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(11, 50) #servo 1 (left right)
pwm2 = GPIO.PWM(12,50) #servo 2 (up down)
pwm.start(0)
pwm2.start(0)
#Servo Functions 
def set_angle_return(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)
    return angle;
def set_angle_return2(angle): #servo 2
    duty = angle / 18 + 2
    GPIO.output(12, True)
    pwm2.ChangeDutyCycle(duty)
    sleep(0.1)
    GPIO.output(12, False)
    pwm2.ChangeDutyCycle(duty)
    return angle;

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(.15)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)
def set_angle2(angle2): #Servo 2
    duty2 = angle2 / 18 + 2
    GPIO.output(12, True)
    pwm2.ChangeDutyCycle(duty2)
    sleep(.15)
    GPIO.output(12, False)
    pwm2.ChangeDutyCycle(duty2)

def init_x_pos():
    duty = 30 / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)
    
def init_y_pos(): #servo 2
    duty = 25 / 18 + 2
    GPIO.output(12, True)
    pwm2.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(12, False)
    pwm2.ChangeDutyCycle(duty)


def move_left(st_angle):
	while (st_angle <= 55):
		set_angle(st_angle)
		st_angle += 3



def move_right(st_angle):
	if (st_angle > 5):
		set_angle(st_angle)
		st_angle -= 3
		move_right(st_angle)
        
def move_up(st_angle2):
	while (st_angle2 <= 55):
		set_angle2(st_angle2)
		st_angle2 += 3

def move_down(st_angle2):
	while (st_angle2 >= 10):
		set_angle2(st_angle2)
		st_angle2 -= 3
	
        
# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
st_angle = 30
st_angle2 = 30 #servo 2

# Handle joystick updates one at a time
while gamepad.isConnected():
    # Wait for the next event
    eventType, control, value = gamepad.getNextEvent()

    # Determine the type
    if eventType == 'BUTTON':
        sleep(.15)
        # Button changed
        if control == buttonTrigger:
            # Trigger
            if value:
                print('Trigger Pressed !')
                
                #pwm.ChangeDutyCycle(100)
            else:
                print('Trigger Released !')
                #pwm.ChangeDutyCycle(0)
                
        elif control == buttonLeft:
            # Left
            if value:
                print('Move Servo Left')
                if(st_angle <= 55):
                    st_angle += 2
                    set_angle(st_angle)
                elif(st_angle >= 53):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)
            else:
                #print('Stop moving Left')
                pwm.ChangeDutyCycle(0)
        elif control == buttonRight:
            # Right
            if value:
                print('Move Servo Right')
                if (st_angle > 5):
                    st_angle -= 2
                    set_angle(st_angle)
                elif(st_angle <= 7):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)

            else:
                #print('Stop moving Right')
                pwm.ChangeDutyCycle(0)
        elif control == buttonUp:
            # Up
            if value:
                print('Move Servo Up')
                if (st_angle2 <= 55):
                    set_angle2(st_angle2)
                    st_angle2 += 2
                elif(st_angle >= 53):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)
            else:
                #print('Stop moving Up')
                pwm2.ChangeDutyCycle(0)
        elif control == buttonDown:
            # Down
            if value:
                print('Move Servo Down')
                if (st_angle2 >= 10):
                    set_angle2(st_angle2)
                    st_angle2 -= 2
                elif(st_angle <= 13):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)
            else:
                #print('Stop moving Down')
                pwm2.ChangeDutyCycle(0)
                
        elif control == buttonExit:
            # Exit
            if value:
                print('Reset')
                init_x_pos()
                pwm.ChangeDutyCycle(0)
                init_y_pos()
                pwm2.ChangeDutyCycle(0)
                
        #else:
            #print(gamepad.getNextEvent())