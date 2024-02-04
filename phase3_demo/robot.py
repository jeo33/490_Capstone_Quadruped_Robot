import math

import numpy as np
from numpy.linalg import norm
from math import acos, degrees


def angle_between_vectors(v1, v2):
    # Calculate the dot product of two vectors
    dot_product = np.dot(v1, v2)

    # Calculate the magnitude (norm) of each vector
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    # Calculate the cosine of the angle between the two vectors
    cos_angle = dot_product / (norm_v1 * norm_v2)

    # Ensure the cosine value is within the valid range [-1, 1] to prevent numerical issues
    cos_angle = max(min(cos_angle, 1), -1)

    # Calculate the angle in radians and then convert to degrees
    angle_radians = math.acos(cos_angle)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees
def SSA_solver(femur,tibia):
    height=femur/np.sqrt(2)+np.sqrt(tibia**2-((femur/np.sqrt(2))**2))
    return height
def SSS_solver(A,B,C):
    var=(A**2+B**2-C**2)/(2*A*B)
    if var>1:
        var=1
    elif var<-1:
        var=-1
    return np.degrees(np.arccos(var))
class robot:
    def __init__(self):
        self.L = 0.075 * 2  # length of robot joints
        self.W = 0.027 * 2  # width of robot joints
        self.coxa = 0.008  # coxa length
        self.femur = 0.044  # femur length
        self.tibia = 0.055  # tibia length
        self.height=SSA_solver(self.femur,self.tibia)
        self.x_norm = np.array([1, 0, 0])
        self.y_norm = np.array([0, 1, 0])
        self.z_norm = np.array([0, 0, 1])
        self.feet_coordinate = np.array([0, 0, 0])

    def solver_R(self,np_array):
        angle_x=angle_between_vectors(np.array([np_array[0], 0, np_array[2]]),self.x_norm)
        theta1=np.degrees(np.pi)-angle_x-SSS_solver(self.femur,np.sqrt(np_array[0]**2+np_array[2]**2),self.tibia,)
        theta2=SSS_solver(self.femur,self.tibia,np.sqrt(np_array[0]**2+np_array[2]**2))
        theta0=90
        return theta0,theta1,theta2
    def solver_L(self,np_array):
        angle_x=angle_between_vectors(np.array([np_array[0], 0, np_array[2]]),self.x_norm)
        theta1=np.degrees(np.pi)-angle_x-SSS_solver(self.femur,np.sqrt(np_array[0]**2+np_array[2]**2),self.tibia,)
        theta2=SSS_solver(self.femur,self.tibia,np.sqrt(np_array[0]**2+np_array[2]**2))
        theta0=90
        return theta0,180-theta1,180-theta2
    def stand(self):
        temp=np.array([0.02,0.0,-0.06])
        right= self.solver_R(temp)
        left= self.solver_L(temp)
        list=right+left+right+left
        return list

    def sit(self):
        temp=np.array([0.055,0.0,-0.044])
        right= self.solver_R(temp)
        left= self.solver_L(temp)
        list=right+left+right+left
        return list
        
    def walk(self):
        temp=[]
        temp1=np.array([0.02,0.0,-0.075])
        temp2=np.array([0.01,0.0,-0.070])
        temp3=np.array([0.02,0.0,-0.065])
        temp4=np.array([0.04,0.0,-0.070])
        temp5=np.array([0.02,0.0,-0.075])
        temp.append(temp1)
        temp.append(temp2)
        temp.append(temp3)
        temp.append(temp4)
        temp.append(temp5)
        list=[]
        stand=np.array([0.02,0.0,-0.075])
        for ite in temp:
            right= self.solver_R(ite)
            left= self.solver_L(ite)            
            right_stand= self.solver_R(stand)
            left_stand= self.solver_L(stand)
            list.append(right+left_stand+right_stand+left)
        for ite in temp:
            right= self.solver_R(ite)
            left= self.solver_L(ite)            
            right_stand= self.solver_R(stand)
            left_stand= self.solver_L(stand)
            list.append(right_stand+left+right+left_stand)
        return list    
    def walk_back(self):
        temp=[]
        temp1=np.array([0.02,0.0,-0.075])
        temp2=np.array([0.01,0.0,-0.070])
        temp3=np.array([0.02,0.0,-0.065])
        temp4=np.array([0.04,0.0,-0.070])
        temp5=np.array([0.02,0.0,-0.075])
        temp.append(temp5)
        temp.append(temp4)
        temp.append(temp3)
        temp.append(temp2)
        temp.append(temp1)
        list=[]
        stand=np.array([0.02,0.0,-0.075])
        for ite in temp:
            right= self.solver_R(ite)
            left= self.solver_L(ite)            
            right_stand= self.solver_R(stand)
            left_stand= self.solver_L(stand)
            list.append(right+left_stand+right_stand+left)
        for ite in temp:
            right= self.solver_R(ite)
            left= self.solver_L(ite)            
            right_stand= self.solver_R(stand)
            left_stand= self.solver_L(stand)
            list.append(right_stand+left+right+left_stand)
        return list




