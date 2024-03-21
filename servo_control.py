from __future__ import division
import time

import Adafruit_PCA9685

class controller:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.servo_min = 122  # Min pulse length out of 4096
        self.servo_max = 650  # Max pulse length out of 4096
        self.pwm.set_pwm_freq(60)
        self.step_time =0.000000000001
        self.flag = True
        self.offset=[0,0,0,
                     0,0,0,
                     0,0,0,
                     0,0,0]
        self.target_angle=[0,0,0,
                           0,0,0,
                           0,0,0,
                           0,0,0]
        #for i in range(0,16):
        #    self.pwm.set_pwm(i,0,int((self.servo_min+self.servo_max)/2))
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
        D = float(self.servo_min) + float(angle) * 528/180
        self.pwm.set_pwm(int(channel), 0, int(D))
#     pwm.set_pwm(channel, 0, pulse)
    def set_pwm_one(self):
        for i in range(0,13):
            self.pwm.set_pwm(int(i), 0,4096)
    def set_pwm_zero(self):
        self.pwm.set_pwm(11,1023,1023)
    def set_winch_pwm_zero(self):
        self.pwm.set_pwm(8,0,4096)
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
        self.set_angle(5, int(target_angle[0]))
        self.set_angle(1, int(target_angle[1]))
        self.set_angle(6, int(target_angle[2]))
        time.sleep(self.step_time)
        self.set_angle(10, int(target_angle[6]))
        self.set_angle(11, int(target_angle[7]))
        self.set_angle(4, int(target_angle[8]))
        time.sleep(self.step_time)
        self.set_angle(2, int(target_angle[3]))
        self.set_angle(3, int(target_angle[4]))
        self.set_angle(0, int(target_angle[5]))
        time.sleep(self.step_time)
        self.set_angle(9, int(target_angle[9]))
        self.set_angle(8, int(target_angle[10]))
        self.set_angle(12, int(target_angle[11]))
        time.sleep(self.step_time)
        #for it in range(0,len(target_angle)):
          # self.set_angle(it, int(target_angle[it])+int(offset[it]))
         #  print(str(it)+"	"+str(len(target_angle)))
          # print(int(target_angle[it])+int(offset[it]))
          # time.sleep(self.step_time)
           



