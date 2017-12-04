# -*- coding: utf-8 -*-
import numpy as np
from Functions import *
import cProfile
import sys



class Particle(object):
    velocity = []
    position = []
    pbest = []
    
    def __init__(self, dimensions):
        self.position = np.random.uniform(-10,10,size=(dimensions,1))
        self.velocity = np.random.uniform(-0.2,0.2,size=(dimensions,1))
        self.pbest = np.copy(self.position)
        self.c1 = 2.05
        self.c2 = 2.05
        
    def updateVelocities(self,gbest, w, dimensions):
        r1 = np.random.sample(size=(dimensions,1))
        r2 = np.random.sample(size=(dimensions,1))

        social = self.c1*r1*(gbest-self.position)
        cognitive = self.c2 * r2 * (self.pbest-self.position)
        self.velocity = (w*self.velocity)+social+cognitive



        # for i in range(dimensions):
        #     #r1 = np.random.uniform(0,1)
        #     #r2 = np.random.uniform(0,1)
        #     r1 = np.random.sample()
        #     r2 = np.random.sample()
        #     social = self.c1 * r1 * (gbest[i] - self.position[i])
        #     cognitive = self.c2 * r2 * (self.pbest[i] - self.position[i])
        #     self.velocity[i] = (w * self.velocity[i]) + social + cognitive
            
    def updatePosition(self, dimensions):

        for i in range(dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            if (self.position[i] > 10 or self.position[i] < -10):
                for i in range(dimensions):
                    self.position[i] = (20*np.random.sample())-10
                break

# def func(points):
#     y = Ackley(points)
#     return y
#
# def monitor(i):
#     if (i%1000 == 0):
#         print
#         sys.stdout.write("Working")
#         sys.stdout.flush()
#     elif (i%100 == 0):
#         sys.stdout.write(".")
#         sys.stdout.flush()
        
# def answer(solution):
#     print
#     print("X1: "+str(solution[0]))
#     print("X2: "+str(solution[1]))
#     if (dimensions == 5):
#         print("X3: "+str(solution[2]))
#         print("X4: "+str(solution[3]))
#         print("X5: "+str(solution[4]))
#     if (dimensions == 10):
#         print("X3: "+str(solution[2]))
#         print("X4: "+str(solution[3]))
#         print("X5: "+str(solution[4]))
#         print("X6: "+str(solution[5]))
#         print("X7: "+str(solution[6]))
#         print("X8: "+str(solution[7]))
#         print("X9: "+str(solution[8]))
#         print("X10: "+str(solution[9]))
#     print("Current Solution: "+str(func(solution)))

def opt(dim,func):

    dimensions = dim
    size = 100
    max_nfc = 3000 * dimensions


    solution = []
    swarm = []
    pbestValArray = np.zeros(size)
    
    w = 0.9
    w_mod = (0.5)/max_nfc

    runs = 5
    run = 0
    allruns = []
    allrunsmax = []
    allrunsmean = []
    allrunsstd = []
    
    print("Starting PSO")
    for i in range(0,size):
        particle = Particle(dimensions)
        swarm.append(particle)

    gbest = np.copy(swarm[0].position)
    gbestVal = func(gbest)
    while (run < runs):
        rundata = []
        rundatamax=[]
        rundatamean = []
        rundatastd = []
        for i in range(max_nfc):
            #pointlist=[]
            #check(i, solution)
            #monitor(i)
            sC = 0
            for s in swarm:
                pbestVal = func(s.pbest)
                pbestValArray[sC] = pbestVal
                sC = sC + 1
                if np.less(pbestVal, gbestVal):
                        gbest = np.copy(s.pbest)
                        gbestVal = func(gbest)
            solution = np.copy(gbest)
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

            if i%100 == 0:
                rundata.append(min(pbestValArray))
                rundatamax.append(max(pbestValArray))
                rundatamean.append(np.mean(pbestValArray))
                rundatastd.append(np.std(pbestValArray))
        run = run + 1
        if run%2==0:
            print('On run: ',run)
        allruns.append(rundata)
        allrunsmax.append(rundatamax)
        allrunsmean.append(rundatamean)
        allrunsstd.append(rundatastd)

    allruns = np.asarray(allruns)
    allrunsmax = np.asarray(allrunsmax)
    allrunsmean = np.asarray(allrunsmean)
    allrunsstd = np.asarray(allrunsstd)
    allruns = np.reshape(allruns,(runs,max_nfc/size) )
    allrunsmax = np.reshape(allrunsmax,(runs,max_nfc/size) )
    allrunsmean = np.reshape(allrunsmean,(runs,max_nfc/size) )
    allrunsstd = np.reshape(allrunsstd,(runs,max_nfc/size) )
    final_runmin =allruns
    final_runmax =allrunsmax
    final_runmean =allrunsmean
    final_runstd =allrunsstd
    plot_runs = np.average(allruns,axis=0) # This is for the plots

    #answer(solution)
    return plot_runs, final_runmin, final_runmax, final_runmean, final_runstd


