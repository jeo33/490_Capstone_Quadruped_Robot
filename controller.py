import hid
import time
from robot import robot
from servo_control import controller
stand=0
walk_init=1
walk=2
walk_final=3
walk_r=4
turn_right=5
turn_left=6

def function_stand():
    print("function_stand triggered")
    controller.set_target_degree(quadruped_robot.stand())
    controller.set_all()
#************************************************************
def function_turn_left_init():
    print("function_turn_left_init triggered")
    controller.set_walk_angle(quadruped_robot.turnleft_init())

def function_turn_left():
    print("function_turn_left triggered")
    controller.set_walk_angle(quadruped_robot.turnleft())

def function_turn_left_final():
    print("function_turn_left_final triggered")
    controller.set_walk_angle(quadruped_robot.turnleft_final())
#************************************************************
def function_turn_right_init():
    print("function_turn_right_init triggered")
    controller.set_walk_angle(quadruped_robot.turnright_init())

def function_turn_right():
    print("function_turn_right triggered")
    controller.set_walk_angle(quadruped_robot.turnright())

def function_turn_right_final():
    print("function_turn_right_final triggered")
    controller.set_walk_angle(quadruped_robot.turnright_final())
#************************************************************

def function_walk_init():
    print("function_walk_init triggered")
    controller.set_walk_angle(quadruped_robot.walk_init())

def function_walk():
    print("function_walk triggered")
    controller.set_walk_angle(quadruped_robot.walk())

def function_walk_final():
    print("function_walk_final triggered")
    controller.set_walk_angle(quadruped_robot.walk_final())
#************************************************************

def function_walk_reverse():
    print("function_walk_reverse triggered")
    controller.set_walk_angle(quadruped_robot.walk_r())

def function_walk_reverse_init():
    print("function_walk_reverse_init triggered")
    controller.set_walk_angle(quadruped_robot.walk_init_r())

def function_walk_reverse_final():
    print("function_walk_reverse_final triggered")
    controller.set_walk_angle(quadruped_robot.walk_final_r())
#************************************************************

def function_up():
    print("function_up triggered")
    controller.set_walk_angle(quadruped_robot.up())
def function_down():
    print("function_down triggered")
    controller.set_walk_angle(quadruped_robot.down())
#************************************************************
    
quadruped_robot=robot()
controller=controller()    
controller.set_target_degree(quadruped_robot.stand())
controller.set_all()
gamepad = hid.device()
gamepad.open(0x0e6f, 0x0214)
gamepad.set_nonblocking(True)
last_state=stand
current_state=stand
#['BR', '0.03', '0', '-0.11']
while True:
    report = gamepad.read(20)
    if report:
        print(report[4])
        #****************************
        if report[4]==0:
            if current_state==walk:
                function_walk()
                current_state=walk
            else:
                function_walk_init()
                function_walk()
                current_state=walk
        #****************************
        elif report[4]==255:
            if current_state==walk_r:
                function_walk_reverse()
                current_state=walk_r
            else:
                function_walk_reverse_init()
                function_walk_reverse()
                current_state=walk_r
        #****************************
        elif report[4]>100 and report[4]<200:
            if current_state==walk:
                function_walk_final()
                current_state=stand
            elif current_state==walk_r:
                function_walk_reverse_final()
                current_state=stand
        #****************************
        elif report[3]==255:
            if current_state==turn_right:
                function_turn_right()
                current_state=turn_right
            else:
                function_turn_right_init()
                function_turn_right()
                current_state=turn_right
        #****************************
        elif report[3]==0:
            if current_state==turn_left:
                function_turn_left()
                current_state=turn_left
            else:
                function_turn_left_init()
                function_turn_left()
                current_state=turn_left
        #****************************
        elif report[3]>100 and report[3]<200:
            if current_state==turn_left:
                function_turn_left_final()
                current_state=stand
            elif current_state==turn_right:
                function_turn_right_final()
                current_state=stand
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
