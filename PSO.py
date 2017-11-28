# -*- coding: utf-8 -*-
import numpy as np
import math
#from Functions import *
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

def Ackley(dim):
    firstSum = 0.0
    secondSum = 0.0
    for c in dim:
        firstSum += c ** 2.0
        secondSum += np.cos(2.0 * math.pi * c)
    n = float(len(dim))
    return -20.0 * math.exp(-0.2 * math.sqrt(firstSum / n)) - math.exp(secondSum / n) + 20 + math.e

def func(points):
    y = Ackley(points)
    return y

def main():
    solution = []
    swarm = []
    
    w = 0.7
    w_mod = (0.4)/max_nfc
    
    for i in range(0,size):
        particle = Particle(dimensions)
        swarm.append(particle)

    gbest = swarm[0].position        
    for i in range(max_nfc):
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
    print(solution)
    print(func(solution))
    return solution
    
main()
