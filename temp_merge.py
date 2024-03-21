
import time
from robot import robot
from servo_control import controller


quadruped_robot=robot()
controller=controller()

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
