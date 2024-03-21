#from evdev import InputDevice, categorize, ecodes
#import threading
import time
from robot import robot
from servo_control import controller
import pygame 

pygame.init()

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

for joystick in joysticks:
    joystick.init()

quadruped_robot=robot()
controller=controller()
#joycon_path_L = '/dev/input/event5'
#joycon_path_R = '/dev/input/event6'

#joycon_L = InputDevice(joycon_path_L)
#joycon_R = InputDevice(joycon_path_R)

def function_forward():
    print("Function A triggered")
    controller.set_walk_angle(quadruped_robot.walk())
    time.sleep(0.02)
def function_backward():
    controller.set_walk_angle(quadruped_robot.walk_back())
    time.sleep(0.02)
def function_sit():
    ...
def function_stand():
    ...



def directional(left, right):
    if left < -0.99:
        print(f'left :{left}')
        function_forward()
        
    elif left > 0.99:
        print(f'left :{left}')
        function_backward()
        
    #if right > 0.05:
    #    print("right")

    #elif right < -0.05:
    #    print("left")

def cross_input():
    controller.set_pwm_zero()
    print("cross")

def circle_input():
    function_sit()

click = True
run = True
while run:

    for joystick in joysticks:
        if joystick.get_button(0): #Cross
            cross_input()
            time.sleep(10)
            
        if joystick.get_button(1): #Circle
            circle_input()
            time.sleep(2)
            
        if joystick.get_button(2): #Square
            square_input()
            time.sleep(2)
            
        if joystick.get_button(3): #Triangle
            triangle_input()
            time.sleep(2)
        
        if joystick.get_button(5): #ps_button
            run = False
            
    
    pygame.event.get()
    for joystick in joysticks:    
        right_x_axis = joystick.get_axis(2)
        left_y_axis = joystick.get_axis(1)
        directional(left_y_axis, right_x_axis)

    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        if event.type == pygame.QUIT:
            run = False
   
pygame.quit()   
 

