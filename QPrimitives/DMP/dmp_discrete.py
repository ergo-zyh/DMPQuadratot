'''
Copyright (C) 2013 Travis DeWolf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from dmp import DMPs

import numpy as np
from decimal import Decimal

class DMPs_discrete(DMPs):
    """An implementation of discrete DMPs"""

    def __init__(self, **kwargs): 
        """
        """

        # call super class constructor
        super(DMPs_discrete, self).__init__(pattern='discrete', **kwargs)

        self.gen_centers()

        # set variance of Gaussian basis functions
        # trial and error to find this spacing
        self.h = np.ones(self.bfs) * self.bfs**1.5 / self.c

        self.check_offset()
        
    def gen_centers(self):
        """Set the centre of the Gaussian basis 
        functions be spaced evenly throughout run time"""

        '''x_track = self.cs.discrete_rollout()
        t = np.arange(len(x_track))*self.dt
        # choose the points in time we'd like centers to be at
        c_des = np.linspace(0, self.cs.run_time, self.bfs)
        self.c = np.zeros(len(c_des))
        for ii, point in enumerate(c_des): 
            diff = abs(t - point)
            self.c[ii] = x_track[np.where(diff == min(diff))[0][0]]'''

        # desired spacings along x
        # need to be spaced evenly between 1 and exp(-ax)
        # lowest number should be only as far as x gets 
        first = np.exp(-self.cs.ax*self.cs.run_time) 
        last = 1.05 - first
        des_c = np.linspace(first,last,self.bfs) 

        self.c = np.ones(len(des_c)) 
        for n in range(len(des_c)): 
            # x = exp(-c), solving for c
            self.c[n] = -np.log(des_c[n])

    def gen_front_term(self, x, dmp_num):
        """Generates the diminishing front term on 
        the forcing term.

        x float: the current value of the canonical system
        dmp_num int: the index of the current dmp
        """
        
        return x * (self.goal[dmp_num] - self.y0[dmp_num])

    def gen_goal(self, y_des): 
        """Generate the goal for path imitation. 
        For rhythmic DMPs the goal is the average of the 
        desired trajectory.
    
        y_des np.array: the desired trajectory to follow
        """

        return y_des[:,-1].copy()
    
    def gen_psi(self, x):
        """Generates the activity of the basis functions for a given 
        state of the canonical system.

        x float: the current state of the canonical system
        """
        
        return np.exp(-self.h * (x - self.c)**2)
        
    def gen_psi(self, x):
        """Generates the activity of the basis functions for a given 
        canonical system rollout. 
        
        x float, array: the canonical system state or path
        """
   
        if isinstance(x, np.ndarray):
            x = x[:,None]
        return np.exp(-self.h * (x - self.c)**2)

    def gen_weights(self, f_target):
        """Generate a set of weights over the basis functions such 
        that the target forcing term trajectory is matched.
        
        f_target np.array: the desired forcing term trajectory
        """

        # calculate x and psi   
        x_track = self.cs.rollout()
        psi_track = self.gen_psi(x_track)

        #efficiently calculate weights for BFs using weighted linear regression
        self.w = np.zeros((self.dmps, self.bfs))
        for d in range(self.dmps):
            # spatial scaling term
            k = (self.goal[d] - self.y0[d])
            for b in range(self.bfs):
                numer = np.sum(x_track * psi_track[:,b] * f_target[:,d])
                denom = np.sum(x_track**2 * psi_track[:,b])
                self.w[d,b] = numer / (k * denom)

#==============================
# Test code
#==============================
if __name__ == "__main__":

    num_bfs = [10, 30, 50, 100, 10000]
    b = 0
    fds = (open('m1.txt','r'),open('m2.txt','r'),open('m3.txt','r'),open('m4.txt','r'),open('m5.txt','r'),open('m6.txt','r'),open('m7.txt','r'),open('m8.txt','r'))
    path1 = [];path2 = [];path3 = [];path4 = [];path5 = [];path6 = [];path7 = [];path8 = []
    while(b<81):
        path1.append(float(fds[0].readline().strip()))
        path2.append(float(fds[1].readline().strip()))
        path3.append(float(fds[2].readline().strip()))
        path4.append(float(fds[3].readline().strip()))
        path5.append(float(fds[4].readline().strip()))
        path6.append(float(fds[5].readline().strip()))
        path7.append(float(fds[6].readline().strip()))
        path8.append(float(fds[7].readline().strip()))
        b = b+1

    import matplotlib.pyplot as plt
    plt.figure(2, figsize=(6,4))
    for ii, bfs in enumerate(num_bfs):
        dmp = DMPs_discrete(dmps=8, bfs=bfs, dt = 0.01252346862728236886893876420061)

        #dmp.imitate_path(y_des=np.array([path1, path2, path3, path4, path5, path6, path7, path8]))
        # change the scale of the movement
        dmp.goal[0] = -82.84; dmp.goal[1] = 101.32; dmp.goal[2] = -89.88; dmp.goal[3] = 100.44; dmp.goal[4] = -100.73; dmp.goal[5] = 100.44; dmp.goal[6] = -90.00; dmp.goal[7] = 100.73 # Stablishing goals that differ slightly with the initial position produces markedly different results
        dmp.imitate_path(y_des=np.array([path1, path2, path3, path4, path5, path6, path7, path8]))
        y_track,dy_track,ddy_track = dmp.rollout()

        plt.figure(2)
        plt.subplot(211)
        plt.plot(y_track[:,6], lw=2)
        plt.subplot(212)
        plt.plot(y_track[:,7], lw=2)

    plt.subplot(211)
    b = 0
    plot1 = []
    plot2 = []
    while(b < len(path1)):
        plot1.append((path7[b]/path7[-1])*dmp.goal[6])
        plot2.append((path8[b]/path8[-1])*dmp.goal[7])
        b = b+1
    a = plt.plot(plot1, 'r--', lw=2)
    plt.title('DMP imitate path')
    plt.xlabel('time (ms)')
    plt.ylabel('system trajectory')
    plt.legend([a[0]], ['desired path'], loc='lower right')
    plt.subplot(212)
    b = plt.plot(plot2, 'r--', lw=2)
    plt.title('DMP imitate path')
    plt.xlabel('time (ms)')
    plt.ylabel('system trajectory')
    plt.legend(['%i BFs'%i for i in num_bfs], loc='lower right')

    plt.tight_layout()
    plt.show()
