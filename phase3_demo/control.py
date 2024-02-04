
import time
from robot import robot
from servo_control import controller



if __name__ == "__main__":
    quadruped_robot=robot()
    controller=controller()

    controller.set_target_degree(quadruped_robot.stand())
    controller.set_all()
    time.sleep(2)
    while 1:
        controller.set_walk_angle(quadruped_robot.walk())
        time.sleep(0.02)
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
