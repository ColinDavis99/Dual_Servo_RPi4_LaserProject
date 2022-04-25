#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time

# Gamepad settings
gamepadType = Gamepad.PS4
buttonTrigger = 'CROSS'
buttonLeft = 'CIRCLE'
buttonExit = 'L2'
buttonRight = 'L1'
buttonDown = 'TRIANGLE'
buttonUp = 'SQUARE'

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
speed = 0.0
steering = 0.0

# Handle joystick updates one at a time
while gamepad.isConnected():
    # Wait for the next event
    eventType, control, value = gamepad.getNextEvent()

    # Determine the type
    if eventType == 'BUTTON':
        # Button changed
        if control == buttonTrigger:
            # Happy button (event on press and release)
            if value:
                print('Trigger Pressed !')
            else:
                print('Trigger Released !')
        elif control == buttonLeft:
            # Beep button (event on press)
            if value:
                print('Move Servo Left')
            else:
                print('Stop moving Left')
        elif control == buttonRight:
            # Beep button (event on press)
            if value:
                print('Move Servo Right')
            else:
                print('Stop moving Right')
        elif control == buttonUp:
            # Beep button (event on press)
            if value:
                print('Move Servo Up')
            else:
                print('Stop moving Up')
        elif control == buttonDown:
            # Beep button (event on press)
            if value:
                print('Move Servo Down')
            else:
                print('Stop moving Down')
                
        elif control == buttonExit:
            # Exit button (event on press)
            if value:
                print('EXIT')
                break
        else:
            print(gamepad.getNextEvent())