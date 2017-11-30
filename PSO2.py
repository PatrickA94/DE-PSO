# -*- coding: utf-8 -*-
import numpy as np
from Functions import *




class Particle(object):
    velocity = []
    position = []
    pbest = []
    c1 = 2.05
    c2 = 2.05

    def __init__(self, dimensions):
        self.position = np.random.uniform(-10, 10, size=(dimensions, 1))
        self.velocity = np.random.uniform(-0.2, 0.2, size=(dimensions, 1))
        self.pbest = self.position
        self.c1 = 2.05
        self.c2 = 2.05

    def updateVelocities(self, gbest, w, dimensions):
        for i in range(dimensions):
            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)
            social = self.c1 * r1 * (gbest[i] - self.position[i])
            cognitive = self.c2 * r2 * (self.pbest[i] - self.position[i])
            self.velocity[i] = (w * self.velocity[i]) + social + cognitive

    def updatePosition(self, dimensions):
        for i in range(dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            if (self.position[i] > 10 or self.position[i] < -10):
                for i in range(dimensions):
                    self.position[i] = np.random.uniform(-10, 10)
                break
                


def opt(dim,func):


    dimensions = dim
    size = 100
    max_nfc = 300 * dimensions

    solution = []
    swarm = []

    w = 0.9
    w_mod = (0.5) / max_nfc

    runs = 3
    run = 0
    allruns = []
    allrunsmax = []
    allrunsmean = []
    allrunsstd = []

    #print("Initializing " + str(size) + " particles...")
    for i in range(0, size):
        particle = Particle(dimensions)
        swarm.append(particle)

    #print("Iterating " + str(max_nfc) + " times...")
    gbest = swarm[0].position
    while (run < runs):
        rundata = []
        rundatamax=[]
        rundatamean = []
        rundatastd = []
        nfc=0
        for i in range(max_nfc):
            pointlist = []
            for s in swarm:
                # func(pbest) < func(gbest)
                pointlist.append(s.position)
                if np.less(func(s.pbest), func(gbest)):
                    gbest = s.pbest
            solution = gbest
            # Update position
            for k in swarm:
                k.updateVelocities(gbest, w, dimensions)
                k.updatePosition(dimensions)
            for l in swarm:
                pbest = l.pbest
                position = l.position
                if np.less(func(position), func(pbest)):
                    l.pbest = l.position
            w = w - w_mod

            if i%100 == 0:
                rundata.append(min(func(pointlist)))
                rundatamax.append(max(func(pointlist)))
                rundatamean.append(np.mean(func(pointlist)))
                rundatastd.append(np.std(func(pointlist)))
        run = run + 1
        if run%10==0:
            print('On run: ',run)
        allruns.append(rundata)
        allrunsmax.append(rundatamax)
        allrunsmean.append(rundatamean)
        allrunsstd.append(rundatastd)


    allruns = np.asarray(allruns)
    allrunsmax = np.asarray(allrunsmax)
    allrunsmean = np.asarray(allrunsmean)
    allrunsstd = np.asarray(allrunsstd)
    allrunsstd = np.asarray(allrunsstd)
    allruns = np.reshape(allruns,(runs,max_nfc/size) )
    allrunsmax = np.reshape(allrunsmax,(runs,max_nfc/size) )
    allrunsmean = np.reshape(allrunsmean,(runs,max_nfc/size) )
    allrunsstd = np.reshape(allrunsstd,(runs,max_nfc/size) )
    final_runmin = allruns[:, -1]
    final_runmax = allrunsmax[:, -1]
    final_runmean = allrunsmean[:, -1]
    final_runstd = allrunsstd[:, -1]
    plot_runs = np.average(allruns, axis=0)  # This is for the plots

    '''
        print("X1: " + str(solution[0]))
        print("X2: " + str(solution[1]))
        if (dimensions == 5):
            print("X3: " + str(solution[2]))
            print("X4: " + str(solution[3]))
            print("X5: " + str(solution[4]))
        if (dimensions == 10):
            print("X3: " + str(solution[2]))
            print("X4: " + str(solution[3]))
            print("X5: " + str(solution[4]))
            print("X6: " + str(solution[5]))
            print("X7: " + str(solution[6]))
            print("X8: " + str(solution[7]))
            print("X9: " + str(solution[8]))
            print("X10: " + str(solution[9]))
        print("Result: " + str(func(solution)))
        return solution
        '''
    return plot_runs, final_runmin, final_runmax, final_runmean, final_runstd



