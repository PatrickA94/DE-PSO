# -*- coding: utf-8 -*-
import numpy as np
from Functions import *
#from Functions import *

class Particle(object):

    def __init__(self, dimensions, c1, c2):
        self.dimensions = dimensions
        self.rangep = {'max':10,'min':-10}
        self.points = np.random.uniform(self.rangep['min'],self.rangep['max'],size=(self.dimensions,1))
        self.c1 = c1
        self.c2 = c2
        self.velocity = np.zeros(dimensions)
        self.pbest = self.points
        
    def localBest(self):
        if func(self.points) < func(self.pbest):
            self.pbest = self.points
        
    def globalBest(self, gbest):
        if func(self.points) < func(gbest):
            return self.points
        else:
            return gbest
        
    def updateVelocities(self,gbest, w):
        for i in range(0,self.dimensions):
            cognitive = np.random.uniform(0,1)*self.c1
            social = np.random.uniform(0,1)*self.c2
            v_new = (w*self.velocity[i]) + (cognitive*(self.pbest[i]-self.points[i])) + (social*(gbest[i]-self.points[i]))
            self.velocity[i] = v_new
            
    def updatePosition(self):
        for i in range(0,self.dimensions):
            self.points[i] = self.points[i] + self.velocity[i]

def func(points):
    y = highCond(points)
    return y

def main():
    #Parameters
    dimensions = 2
    pop = 100
    c1 = 2.05
    c2 = 2.05
    w = 0.9
    nfc = 0
    max_nfc = 100*dimensions
    w_mod = ((0.9-0.4)/max_nfc)
	
    #Initialization of swarm
    population = []
    for i in range(0,pop):
        p = Particle(dimensions, c1, c2)
        population.append(p)
        
    #Determine initial gbest
    gbest = population[0].pbest
    for p in population:
        if func(p.pbest) < func(gbest):
            gbest = p.pbest

    while( nfc < max_nfc ):
        for i in population:
            i.updateVelocities(gbest, w)
            i.localBest()
            gbest = i.globalBest(gbest)
            i.updatePosition()
        nfc = nfc + 1
        w = w - w_mod
        
    print("Global Best: " + str(gbest))
    print("Global Best Val: " + str(func(gbest)))

main()