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
#Functions to be done when button press ie drum smack

	
        
# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
#any values necessary to initialize ur program 

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

            else:
                print('Stop moving Left')

        elif control == buttonRight:
            # Right
            if value:
                print('Move Servo Right')

            else:
                print('Stop moving Right')
        elif control == buttonUp:
            # Up
            if value:
                print('Move Servo Up')
            else:
                print('Stop moving Up')
        elif control == buttonDown:
            # Down
            if value:
                print('Move Servo Down'))
            else:
                print('Stop moving Down')

                
        elif control == buttonExit:
            # Exit
            if value:
                print('Reset')
        else:
            print(gamepad.getNextEvent())