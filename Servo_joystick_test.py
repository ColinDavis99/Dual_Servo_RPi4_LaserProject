#!/usr/bin/python

import pygame
import os
#from pygame import joystick, event

pygame.init()
#joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print('Initialized Joystick : %s' % j.get_name())

pulse_max = [240,240,240,240,240,240,240,240]
pulse_neut = [150,150,150,150,150,150,150,150]
pulse_min = [60,60,60,60,60,60,60,60]

os.system("sudo sbload")
sb=open("/dev/servoblaster","w")
for axis in range(0,8):
    sb.write(str(axis)+"="+str(pulse_neut[axis])+"\n")    
    sb.flush()
    #print(str(axis)+"="+str(pulse_neut[axis])+"\n")
print('Initialized Servoblaster')

joy_dead = [.05,.05,.05,.05,.05,.05,.05,.05]
joy_startup = [.05,.05,.05,.05,.05,.05,.05,.05]
joy_exp = [1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]

def exp_joy(joy_val, exp, dead, startup):
    live = abs(joy_val)-dead
    if live <= 0:
        return 0
    else:
        return (joy_val/abs(joy_val))*(startup+((1-startup)*pow(live,exp)/pow((1-dead),exp)))

def axis2servo(axis,value):
    if value == 0:
        return pulse_neut[axis]
    elif value > 0:
        return int(pulse_neut[axis]+value*(pulse_max[axis]-pulse_neut[axis]))
    else:
        return int(pulse_neut[axis]+value*(pulse_neut[axis]-pulse_min[axis]))

try:
    while True:
        pygame.event.pump()
        for i in range(0, j.get_numaxes()):
            if j.get_axis(i) != 0.00:
                axis_val = j.get_axis(i)
                curved_val = exp_joy(axis_val,joy_exp[i],joy_dead[i],joy_startup[i])
                servo_pulse = axis2servo(i,curved_val)
                #print('Axis', i,'reads', axis_val, 'exponentialized', curved_val, 'pulse', servo_pulse)
                sb.write(str(i)+"="+str(servo_pulse)+"\n")
                sb.flush()
        for i in range(0, j.get_numbuttons()):
            if j.get_button(i) != 0:
                print('Button %i reads %i' % (i, j.get_button(i)))
except KeyboardInterrupt:
    print('Ending program.')
    j.quit()
    sb.close()
    os.system("sudo sbunload")