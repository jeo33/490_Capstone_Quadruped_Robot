
import time
from robot import robot
from servo_control import controller  
import numpy as np


if __name__ == "__main__":
    quadruped_robot=robot()
    controller=controller()
    controller.set_target_degree(quadruped_robot.stand())
    controller.set_all()
    #controller.set_pwm_zero()
    time.sleep(2)
    while 1:
        x = input("\n command:").split()
        print(x)
        if len(x) == 1:
            if x[0]=='sit':
                controller.set_target_degree(quadruped_robot.sit())
                controller.set_all()
            elif x[0]=='stand':
                controller.set_target_degree(quadruped_robot.stand())
                controller.set_all()
            elif x[0]=='off':
                controller.set_pwm_zero()
                time.sleep(0.02)
            elif x[0]=='in':
                controller.set_angle(12,130)
                time.sleep(0.02)
            elif x[0]=='walk':
                for it in range(0,5):
                    controller.set_walk_angle(quadruped_robot.walk())
                time.sleep(0.02)
            elif x[0]=='init':
                controller.set_walk_angle(quadruped_robot.walk_init())
                time.sleep(0.02)
            elif x[0]=='down':
                controller.set_walk_angle(quadruped_robot.down())
                time.sleep(0.02)
            elif x[0]=='up':
                controller.set_walk_angle(quadruped_robot.up())
                time.sleep(0.02)
            elif x[0]=='final':
                controller.set_walk_angle(quadruped_robot.walk_final())
                time.sleep(0.02)
            elif x[0]=='cycle':
                controller.set_walk_angle(quadruped_robot.walk_init())
                for i in range(0,15):
                    controller.set_walk_angle(quadruped_robot.walk())
                controller.set_walk_angle(quadruped_robot.walk_final())
                
                
            elif x[0]=='walk_r':
                for it in range(0,5):
                    controller.set_walk_angle(quadruped_robot.walk_r())
                time.sleep(0.02)
            elif x[0]=='init_r':
                controller.set_walk_angle(quadruped_robot.walk_final_r())
                time.sleep(0.02)
            elif x[0]=='final_r':
                controller.set_walk_angle(quadruped_robot.walk_init_r())
                time.sleep(0.02)
            elif x[0]=='cycle_r':
                controller.set_walk_angle(quadruped_robot.walk_final_r())
                for i in range(0,15):
                    controller.set_walk_angle(quadruped_robot.walk_r())
                controller.set_walk_angle(quadruped_robot.walk_init_r())
                
                
            elif x[0]=='turnleft':
                for it in range(0,5):
                    controller.set_walk_angle(quadruped_robot.turnleft())
                time.sleep(0.02)
            elif x[0]=='turnleft_init':
                controller.set_walk_angle(quadruped_robot.turnleft_init())
                time.sleep(0.02)
            elif x[0]=='turnleft_final':
                controller.set_walk_angle(quadruped_robot.turnleft_final())
                time.sleep(0.02)
            elif x[0]=='cycle_turnleft':
                controller.set_walk_angle(quadruped_robot.turnleft_init())
                controller.set_walk_angle(quadruped_robot.turnleft())
                controller.set_walk_angle(quadruped_robot.turnleft_final())
                           
                
            elif x[0]=='turnright':
                for it in range(0,5):
                    controller.set_walk_angle(quadruped_robot.turnright())
                time.sleep(0.02)
            elif x[0]=='turnright_init':
                controller.set_walk_angle(quadruped_robot.turnright_init())
                time.sleep(0.02)
            elif x[0]=='turnright_final':
                controller.set_walk_angle(quadruped_robot.turnright_final())
                time.sleep(0.02)
            elif x[0]=='cycle_turnright':
                controller.set_walk_angle(quadruped_robot.turnright_init())
                controller.set_walk_angle(quadruped_robot.turnright())
                controller.set_walk_angle(quadruped_robot.turnright_final())
                
            elif x[0]=='stop':
                controller.set_pwm_one()
                time.sleep(0.02)
            elif x[0]=='out':
                controller.set_angle(12,50)
                time.sleep(0.02)
        elif len(x) == 2:
            controller.set_angle(x[0], x[1])
        elif len(x) == 4:
            if x[0].upper()=='FR':
                temp= np.array([float(x[1]), float(x[2]), float(x[3])])
                an=quadruped_robot.solver_R(temp)
                print(an)
                controller.set_angle(10, an[0])
                controller.set_angle(11, an[1])
                controller.set_angle(4, an[2])
            elif x[0].upper()=='FL':
                temp= np.array([float(x[1]), float(x[2]), float(x[3])])
                an=quadruped_robot.solver_L(temp)
                print(an)
                controller.set_angle(9, an[0])
                controller.set_angle(8, an[1])
                controller.set_angle(12, an[2])
            elif x[0].upper()=='BR':
                temp=np.array([float(x[1]), float(x[2]), float(x[3])])
                an=quadruped_robot.solver_R(temp)
                print(an)
                controller.set_angle(5, an[0])
                controller.set_angle(1, an[1])
                controller.set_angle(6, an[2])
            elif x[0].upper()=='BL':
                temp=np.array([float(x[1]), float(x[2]), float(x[3])])
                an=quadruped_robot.solver_L(temp)
                print(an)
                controller.set_angle(2, an[0])
                controller.set_angle(3, an[1])
                controller.set_angle(0, an[2])
    
print('Moving servo on channel0, press Ctrl-C to quit...')
#
# solver = robot()
# while flag:
#     x = input().split()
#     print(x)
#
#     if len(x) == 1:
#         command(x[0])
#     elif len(x) == 2:
#         set_angle(x[0], x[1])
#     elif len(x) == 3:
#         fir, se = solver.solver_FR(float(x[0]), float(x[2]))
#         y1, y2 = theta_to_servo(fir, se)
#         set_angle(7, y1)
#         set_angle(8, y2)
# print('Moving servo on channel0, press Ctrl-C to quit...')
# # for i in range(0,20000):
#
# # pwm.set_pwm(0,0,410)
