from DMP.dmp_discrete import *
import pypot.primitive
import time
import numpy as np

class DMPQ(pypot.primitive.Primitive):

    def __init__(self, robot):
        self.robot = robot
        self.dmp = DMPs_discrete(dmps = 8, bfs = 10000, dt = 0.01252346862728236886893876420061)
        pypot.primitive.Primitive.__init__(self, robot)
        fds = (open('m1.txt', 'r'), open('m2.txt', 'r'), open('m3.txt', 'r'), open('m4.txt', 'r'), open(
            'm5.txt', 'r'), open('m6.txt', 'r'), open('m7.txt', 'r'), open('m8.txt', 'r'))
        path1 = []
        path2 = []
        path3 = []
        path4 = []
        path5 = []
        path6 = []
        path7 = []
        path8 = []
        b = 0
        while(b < 81):
            path1.append(float(fds[0].readline().strip()))
            path2.append(float(fds[1].readline().strip()))
            path3.append(float(fds[2].readline().strip()))
            path4.append(float(fds[3].readline().strip()))
            path5.append(float(fds[4].readline().strip()))
            path6.append(float(fds[5].readline().strip()))
            path7.append(float(fds[6].readline().strip()))
            path8.append(float(fds[7].readline().strip()))
            b = b + 1
        self.dmp.goal[0] = -82.84
        self.dmp.goal[1] = 101.32
        self.dmp.goal[2] = -89.88
        self.dmp.goal[3] = 100.44
        self.dmp.goal[4] = -100.73
        self.dmp.goal[5] = 100.44
        self.dmp.goal[6] = -90.00
        self.dmp.goal[7] = 100.73
        #self.dmp.timesteps = 80
        self.dmp.imitate_path(y_des=np.array([path1, path2, path3, path4, path5, path6, path7, path8]))
        self.m8 = self.robot.motors[7]
        self.m7 = self.robot.motors[6]
        self.m6 = self.robot.motors[5]
        self.m5 = self.robot.motors[4]
        self.m4 = self.robot.motors[3]
        self.m3 = self.robot.motors[2]
        self.m2 = self.robot.motors[1]
        self.m1 = self.robot.motors[0]
    def run(self):
        
        st = np.empty(8)
        while self.elapsed_time < 3.7:
            
            self.y_track, self.dy_track, self.ddy_track = self.dmp.step(tau = 2.1)
            #the idea is to give step() feedback about our current status, but since
            #we're controlling on the motor space, rather than the position space, 
            #this will only lead to the robot growing to a halt. If we were 
            #measuring an actual distance to an external target, then it would be
            #highly useful to do so.
            self.m1.goto_position(self.y_track[0], 0.2, control=None, wait=False)
            self.m2.goto_position(self.y_track[1], 0.2, control=None, wait=False)
            self.m3.goto_position(self.y_track[2], 0.2, control=None, wait=False)
            self.m4.goto_position(self.y_track[3], 0.2, control=None, wait=False)
            self.m5.goto_position(self.y_track[4], 0.2, control=None, wait=False)
            self.m6.goto_position(self.y_track[5], 0.2, control=None, wait=False)
            self.m7.goto_position(self.y_track[6], 0.2, control=None, wait=False)
            self.m8.goto_position(self.y_track[7], 0.2, control=None, wait=False)
            time.sleep(0.1)
            st[0]= (self.m1.present_position)
            st[1]= (self.m2.present_position)
            st[2]= (self.m3.present_position)
            st[3]= (self.m4.present_position)
            st[4]= (self.m5.present_position)
            st[5]= (self.m6.present_position)
            st[6]= (self.m7.present_position)
            st[7]= (self.m8.present_position)
        self.dmp.reset_state()
