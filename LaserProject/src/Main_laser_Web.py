#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import serial
import string
import time
import Gamepad
import time
import json
import subprocess
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
# Gamepad settings
gamepadType = Gamepad.PS4
buttonTrigger = 'CROSS'
buttonLeft = 'CIRCLE'
buttonExit = 'L2'
buttonRight = 'L1'
buttonDown = 'TRIANGLE'
buttonUp = 'SQUARE'
buttonBalloonReset = 'R1'
# Servo Settings
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(11, 50) #servo 1 (left right)
pwm2 = GPIO.PWM(12,50) #servo 2 (up down)
pwm.start(0)
pwm2.start(0)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

phaseA = 16
GPIO.setup(phaseA, GPIO.OUT)
enable = 18
GPIO.setup(enable, GPIO.OUT)
standby = 22
GPIO.setup(standby, GPIO.OUT)
triggerpull= False
# GPIO Detect EVent
#to go into trigger function#####


#####################################
# GPIO.output(standby, GPIO.HIGH)
# GPIO.output(enable, GPIO.HIGH)
# GPIO.output(phaseA, GPIO.LOW)
# sleep(2)
# GPIO.output(phaseA, GPIO.HIGH)
# sleep(2)
# GPIO.output(enable, GPIO.LOW)
# GPIO.output(phaseA, GPIO.LOW)
# GPIO.output(standby, GPIO.LOW)
########################################

# Webserver Data

controls_data = {
    'up_active': 0,
    'down_active': 0,
    'left_active': 0,
    'right_active': 0,
    'firing_active': 0
}

balloons_data = {
    'top_left_popped': 0,
    'top_mid_popped': 0,
    'top_right_popped': 0,
    'bottom_left_popped': 0,
    'bottom_mid_popped': 0,
    'bottom_right_popped': 0,
}

topLeft = False
topMid = False
topRight = False
bottomLeft = False
bottomMid = False
bottomRight = False
# Webserver Functions

def update_controls_data(button_type, state, addDelay):
    if (addDelay):
        time.sleep(0.5)
    if (button_type == "left"):
        if (state == 0):
            updated_data = {'left_active': 0}
            controls_data.update(updated_data)
        elif (state == 1):
            updated_data = {'left_active': 1}
            controls_data.update(updated_data)
    elif (button_type == "right"):
        if (state == 0):
            updated_data = {'right_active': 0}
            controls_data.update(updated_data)
        elif (state == 1):
            updated_data = {'right_active': 1}
            controls_data.update(updated_data)
    elif (button_type == "up"):
        if (state == 0):
            updated_data = {'up_active': 0}
            controls_data.update(updated_data)
        elif (state == 1):
            updated_data = {'up_active': 1}
            controls_data.update(updated_data)
    elif (button_type == "down"):
        if (state == 0):
            updated_data = {'down_active': 0}
            controls_data.update(updated_data)
        elif (state == 1):
            updated_data = {'down_active': 1}
            controls_data.update(updated_data)
    elif (button_type == "firing"):
        if (state == 0):
            updated_data = {'firing_active': 0}
            controls_data.update(updated_data)
        elif (state == 1):
            updated_data = {'firing_active': 1}
            controls_data.update(updated_data)

def write_controls_json():
    json_string = json.dumps(controls_data)
    # Using a JSON string
    with open('controls_data.json', 'w') as outfile:
        outfile.write(json_string)
    subprocess.call(['sh', './copy_data.sh'])

def update_balloons_data(balloon, state, addDelay):
    if (addDelay):
        time.sleep(0.5)
    if (balloon == "top_left"):
        if (state == 0):
            updated_data = {'top_left_popped': 0}
            balloons_data.update(updated_data)
        elif (state == 1):
            updated_data = {'top_left_popped': 1}
            balloons_data.update(updated_data)
    elif (balloon == "top_mid"):
        if (state == 0):
            updated_data = {'top_mid_popped': 0}
            balloons_data.update(updated_data)
        elif (state == 1):
            updated_data = {'top_mid_popped': 1}
            balloons_data.update(updated_data)
    elif (balloon == "top_right"):
        if (state == 0):
            updated_data = {'top_right_popped': 0}
            balloons_data.update(updated_data)
        elif (state == 1):
            updated_data = {'top_right_popped': 1}
            balloons_data.update(updated_data)
    elif (balloon == "bottom_left"):
        if (state == 0):
            updated_data = {'bottom_left_popped': 0}
            balloons_data.update(updated_data)
        elif (state == 1):
            updated_data = {'bottom_left_popped': 1}
            balloons_data.update(updated_data)
    elif (balloon == "bottom_mid"):
        if (state == 0):
            updated_data = {'bottom_mid_popped': 0}
            balloons_data.update(updated_data)
        elif (state == 1):
            updated_data = {'bottom_mid_popped': 1}
            balloons_data.update(updated_data)
    elif (balloon == "bottom_right"):
        if (state == 0):
            updated_data = {'bottom_right_popped': 0}
            balloons_data.update(updated_data)
        elif (state == 1):
            updated_data = {'bottom_right_popped': 1}
            balloons_data.update(updated_data)


def write_balloons_json():
    json_string = json.dumps(balloons_data)
    # Using a JSON string
    with open('balloons_data.json', 'w') as outfile:
        outfile.write(json_string)
    subprocess.call(['sh', './copy_balloon_data.sh'])


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
    duty = 28 / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)

def init_y_pos(): #servo 2
    duty = 21 / 18 + 2
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
    GPIO.output(29, GPIO.HIGH)
    # Wait for the next event
    eventType, control, value = gamepad.getNextEvent()

    # Determine the type
    if eventType == 'BUTTON':
        sleep(.15)
        # Button changed
        if control == buttonTrigger:
            # Trigger
            if value:
                #opening serial port
                print("Trigger pressed")
                GPIO.output(29, GPIO.LOW)
                update_controls_data("firing", 0, False)
                write_controls_json()
                GPIO.output(standby, GPIO.HIGH)
                GPIO.output(enable, GPIO.HIGH)
                GPIO.output(phaseA, GPIO.HIGH)
                sleep(.5)
                GPIO.output(phaseA, GPIO.LOW)
                sleep(.5)
                GPIO.output(enable, GPIO.LOW)
                GPIO.output(phaseA, GPIO.LOW)
                GPIO.output(standby, GPIO.LOW)
                ser=serial.Serial('/dev/ttyACM0', 9600)
                i = 12
                while True :
                    serialdata=ser.readline()
                    if "One" in str(serialdata): #Will change to filter based on threshold and determine if on or off
                        res = [int(i) for i in serialdata.split() if i.isdigit()][0]
                        #print(res)
                        i -=1
                        if res < 150:
                            print('Balloon One has Popped')
                            topLeft = True
                            if i < 1:
                                break
                        else:
                            print('Balloon One Still there')
                    if "Two" in str(serialdata):
                        res2 = [int(i) for i in serialdata.split() if i.isdigit()][0]
                        #print(res2)
                        i -= 1
                        if res2 < 150:
                            print('Balloon Two has Popped')
                            topMid = True
                            if i < 1:
                                break
                        else:
                            print('Balloon Two Still there')
                    elif "Three" in str(serialdata):
                        res3 = [int(i) for i in serialdata.split() if i.isdigit()][0]
                        #print(res3)
                        i -= 1
                        if res3 < 150:
                            print('Balloon Three has Popped')
                            topRight = True
                            if i < 1:
                                break
                        else:
                            print('Balloon Three Still there')
                    elif "Four" in str(serialdata):
                        res4 = [int(i) for i in serialdata.split() if i.isdigit()][0]
                        #print(res4)
                        i -= 1
                        if res4 < 150:
                            print('Balloon Four has Popped')
                            bottomLeft = True
                            if i < 1:
                                break
                        else:
                            print('Balloon Four Still there')
                    elif "Five" in str(serialdata):
                        res5 = [int(i) for i in serialdata.split() if i.isdigit()][0]
                        i -= 1
                        #print(res5)
                        if res5 < 150:
                            print('Balloon Five has Popped')
                            bottomMid = True
                            if i < 1:
                                break
                        else:
                            print('Balloon Five Still there')

                    elif "Six" in str(serialdata):
                        res6 = [int(i) for i in serialdata.split() if i.isdigit()][0]
                        #print(res6)
                        i -= 1 #run loop 5 times, expecting 5 sets of data, then except next input
                        #print(i)
                        if res6 < 150:
                            print('Balloon Six has Popped')
                            bottomRight = True
                            if i < 1:
                                break
                        else:
                            print('Balloon Six Still there')
                            if i < 1:
                                break

                    #print(serialdata)
                #read serial data and print it on screen

                #pwm.ChangeDutyCycle(100)
            else:
                #ser.close()
                print('Trigger Released !')
                GPIO.output(29, GPIO.HIGH)
                update_controls_data("firing", 0, False)
                #write_controls_json()

                if (topLeft):
                    update_balloons_data("top_left", 1, False)
                if (topMid):
                    update_balloons_data("top_mid", 1, False)
                if (topRight):
                    update_balloons_data("top_right", 1, False)
                if (bottomLeft):
                    update_balloons_data("bottom_left", 1, False)
                if (bottomMid):
                    update_balloons_data("bottom_mid", 1, False)
                if (bottomRight):
                    update_balloons_data("bottom_right", 1, False)
                write_balloons_json()
                #pwm.ChangeDutyCycle(0)

        elif control == buttonLeft:
            # Left
            if value:
                print('Move Servo Left')
                update_controls_data("left", 1, False)
                #write_controls_json()

                if(st_angle <= 55):
                    #pwm.ChangeDutyCycle(5)
                    st_angle += 3
                    set_angle(st_angle)
                elif(st_angle >= 53):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)
                update_controls_data("left", 0, False)
                #write_controls_json()
            else:
                #print('Stop moving Left')
                pwm.ChangeDutyCycle(0)
        elif control == buttonRight:
            # Right
            if value:
                print('Move Servo Right')
                update_controls_data("right", 1, False)
                #write_controls_json()
                if (st_angle > 5):
                    #pwm.ChangeDutyCycle(2)
                    st_angle -= 3
                    set_angle(st_angle)
                elif(st_angle <= 7):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)
                update_controls_data("right", 0, False)
                #write_controls_json()

            else:
                #print('Stop moving Right')
                pwm.ChangeDutyCycle(0)
        elif control == buttonUp:
            # Up
            if value:
                print('Move Servo Up')
                update_controls_data("up", 1, False)
                #write_controls_json()
                if (st_angle2 <= 55):
                    set_angle2(st_angle2)
                    st_angle2 += 2
                elif(st_angle >= 53):
                    print('Boundary Reached')
                    pwm.ChangeDutyCycle(0)
                update_controls_data("up", 0, False)
                #write_controls_json()
            else:
                #print('Stop moving Up')
                pwm2.ChangeDutyCycle(0)
        elif control == buttonDown:
            # Down
            if value:
                print('Move Servo Down')
                update_controls_data("down", 1, False)
                #write_controls_json()
                if (st_angle2 >= 10):
                    set_angle2(st_angle2)
                    st_angle2 -= 2
                elif(st_angle <= 13):
                    print('Boundary Reached')
                update_controls_data("down", 0, False)
                #write_controls_json()
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
                update_controls_data("up", 0, False)
                update_controls_data("down", 0, False)
                update_controls_data("left", 0, False)
                update_controls_data("right", 0, False)
                update_controls_data("firing", 0, False)
                write_controls_json()

        elif control == buttonBalloonReset:
            # Exit
            if value:
                print('Balloon Map Reset')
                update_balloons_data("top_left", 0, False)
                update_balloons_data("top_mid", 0, False)
                update_balloons_data("top_right", 0, False)
                update_balloons_data("bottom_left", 0, False)
                update_balloons_data("bottom_mid", 0, False)
                update_balloons_data("bottom_right", 0, False)
                topLeft = False
                topMid = False
                topRight = False
                bottomLeft = False
                bottomMid = False
                bottomRight = False
                write_balloons_json()

        #else:
            #print(gamepad.getNextEvent())
