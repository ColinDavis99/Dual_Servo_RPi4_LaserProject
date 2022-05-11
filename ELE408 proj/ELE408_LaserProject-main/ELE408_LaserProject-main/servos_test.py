# Example Servo Code

import RPi.GPIO as GPIO
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

def move_left(st_angle):
	while (st_angle <= 55):
		st_angle += 3
		set_angle(st_angle)


def move_right(st_angle):
	while (st_angle >= 15):
		st_angle -= 3
		set_angle(st_angle)	

init_x_pos()
sleep(1)
st_angle = 30
set_angle(st_angle)
move_left(st_angle)
init_x_pos()
sleep(1)
st_angle = 30
move_right(st_angle)
init_x_pos()






	

# End program conditions
pwm.stop()
GPIO.cleanup()
