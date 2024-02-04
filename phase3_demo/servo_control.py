from __future__ import division
import time

import Adafruit_PCA9685

class controller:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.servo_min = 170  # Min pulse length out of 4096
        self.servo_max = 670  # Max pulse length out of 4096
        self.pwm.set_pwm_freq(60)
        self.step_time = 0.005
        self.flag = True
        self.offset=[-30,0,0,
                     -10,0,0,
                     -10,0,0,
                     0,0,0]
        self.target_angle=[0,0,0,
                           0,0,0,
                           0,0,0,
                           0,0,0]
    def set_target_degree(self,list_of_12):
        self.target_angle =list_of_12
        print(self.target_angle)

# def set_servo_pulse(channel, pulse):
#     pulse_length = 1000000    # 1,000,000 us per second
#     pulse_length //= 60       # 60 Hz
#     print('{0}us per period'.format(pulse_length))
#     pulse_length //= 4096     # 12 bits of resolution
#     print('{0}us per bit'.format(pulse_length))
#     pulse *= 1000
#     pulse //= pulse_length
#     pwm.set_pwm(channel, 0, pulse)
    def set_angle(self,channel, angle):
        D = float(170.0) + float(angle) * 2.78
        self.pwm.set_pwm(int(channel), 0, int(D))
    def set_walk_angle(self,list_4_ites):
        for it in list_4_ites:
            self.set_target_degree(it)
            self.set_all()
    def set_all(self):
        target_angle=self.target_angle
        offset=self.offset
        print(target_angle)
        print("target_angle")
        print(offset)
        print("offset")
        for it in range(0,len(target_angle)):
           self.set_angle(it, int(target_angle[it])+int(offset[it]))
           print(str(it)+"	"+str(len(target_angle)))
           print(int(target_angle[it])+int(offset[it]))
           time.sleep(self.step_time)
           



