# -*- coding: utf-8 -*-
import numpy as np
from Functions import *
dimensions = 2
size = 100
max_nfc = 5000*dimensions
c1 = 2.05
c2 = 2.05



class Particle(object):
    velocity = []
    position = []
    pbest = []
    
    def __init__(self, dimensions):
        self.position = np.random.uniform(-10,10,size=(dimensions,1))
        self.velocity = np.random.uniform(-0.2,0.2,size=(dimensions,1))
        self.pbest = self.position
        
    def updateVelocities(self,gbest, w):
        for i in range(dimensions):
            r1 = np.random.uniform(0,1)
            r2 = np.random.uniform(0,1)
            social = c1 * r1 * (gbest[i] - self.position[i])
            cognitive = c2 * r2 * (self.pbest[i] - self.position[i])
            self.velocity[i] = (w * self.velocity[i]) + social + cognitive
            
    def updatePosition(self):
        for i in range(dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            if (self.position[i] > 10):
                self.position[i] = 10
                self.velocity[i] = -(self.velocity[i]) 
            elif (self.position[i] < -10):
                self.position[i] = -10
                self.velocity[i] = -(self.velocity[i])

def func(points):
    y = weirerstrass(points)
    return y

def main():
    solution = []
    swarm = []
    
    w = 0.9
    w_mod = (0.5)/max_nfc
    
    print("Initializing "+str(size)+" particles...")
    for i in range(0,size):
        particle = Particle(dimensions)
        swarm.append(particle)

    print("Iterating "+str(max_nfc)+" times...")
    gbest = swarm[0].position        
    for i in range(max_nfc):
        if (i%100 == 0):
            print("Iterating: "+str(i)+"/"+str(max_nfc))
        for s in swarm:
            pbest = s.pbest
            if func(pbest) < func(gbest):
                    gbest = pbest   
        solution = gbest
        # Update position
        for k in swarm:
            k.updateVelocities(gbest, w)
            k.updatePosition()
        for l in swarm:
            pbest = l.pbest
            position = l.position
            if func(position) < func(pbest):
                swarm[l].pbest = swarm[l].position
        w = w - w_mod
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
    print("Result: "+str(func(solution)))
    return solution
    
main()
