# -*- coding: utf-8 -*-
import numpy as np
from Functions import *
import cProfile
import sys

dimensions = 2
size = 100
max_nfc = 3000*dimensions
c1 = 2.05
c2 = 2.05



class Particle(object):
    velocity = []
    position = []
    pbest = []
    
    def __init__(self, dimensions):
        self.position = np.random.uniform(-10,10,size=(dimensions,1))
        self.velocity = np.random.uniform(-0.2,0.2,size=(dimensions,1))
        self.pbest = np.copy(self.position)
        
    def updateVelocities(self,gbest, w, dimensions):
        for i in range(dimensions):
            #r1 = np.random.uniform(0,1)
            #r2 = np.random.uniform(0,1)
            r1 = np.random.sample()
            r2 = np.random.sample()
            social = c1 * r1 * (gbest[i] - self.position[i])
            cognitive = c2 * r2 * (self.pbest[i] - self.position[i])
            self.velocity[i] = (w * self.velocity[i]) + social + cognitive
            
    def updatePosition(self, dimensions):
        for i in range(dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            if (self.position[i] > 10 or self.position[i] < -10):
                for i in range(dimensions):
                    self.position[i] = (20*np.random.sample())-10
                break

def func(points):
    y = Ackley(points)
    return y
        
def monitor(i):
    if (i%1000 == 0):
        print
        sys.stdout.write("Working")
        sys.stdout.flush()
    elif (i%100 == 0):
        sys.stdout.write(".")
        sys.stdout.flush()
        
def answer(solution):
    print
    print("X1: "+str(solution[0]))
    print("X2: "+str(solution[1]))
    if (dimensions == 5):
        print("X3: "+str(solution[2]))
        print("X4: "+str(solution[3]))
        print("X5: "+str(solution[4]))
    if (dimensions == 10):
        print("X3: "+str(solution[2]))
        print("X4: "+str(solution[3]))
        print("X5: "+str(solution[4]))
        print("X6: "+str(solution[5]))
        print("X7: "+str(solution[6]))
        print("X8: "+str(solution[7]))
        print("X9: "+str(solution[8]))
        print("X10: "+str(solution[9]))
    print("Current Solution: "+str(func(solution)))

def main():
    solution = []
    swarm = []
    pbestValArray = np.zeros(size)
    
    w = 0.9
    w_mod = (0.5)/max_nfc
    
    print("Initializing "+str(size)+" particles...")
    for i in range(0,size):
        particle = Particle(dimensions)
        swarm.append(particle)

    print("Iterating "+str(max_nfc)+" times...")
    gbest = np.copy(swarm[0].position)
    gbestVal = func(gbest)
    for i in range(max_nfc):
        #check(i, solution)
        monitor(i)
        sC = 0
        for s in swarm:
            pbestVal = func(s.pbest)
            pbestValArray[sC] = pbestVal
            sC = sC + 1
            if np.less(pbestVal, gbestVal):
                    gbest = np.copy(s.pbest)
                    gbestVal = func(gbest)
        solution = np.copy(gbest)
        # Get Solution Every 100 Iterations
        if (i%100 == 0):
            # DO WHAT YOU NEED TO DO WITH gbestVal
        # Update position
        for k in swarm:
            k.updateVelocities(gbest, w, dimensions)
            k.updatePosition(dimensions)
        lC = 0
        for l in swarm:
            pbestEval = pbestValArray[lC]
            lC = lC + 1
            if np.less(func(l.position), pbestEval):
                l.pbest = np.copy(l.position)
        w = w - w_mod
    answer(solution)
    return solution

main()
