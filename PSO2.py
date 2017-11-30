# -*- coding: utf-8 -*-
import numpy as np
from Functions import *

dimensions = 2
size = 100
max_nfc = 3000 * dimensions
c1 = 2.05
c2 = 2.05


class Particle(object):
    velocity = []
    position = []
    pbest = []

    def __init__(self, dimensions):
        self.position = np.random.uniform(-10, 10, size=(dimensions, 1))
        for i in range(dimensions):
            self.position[i] = float("{0:.10f}".format(float(self.position[i])))
        self.velocity = np.random.uniform(-0.2, 0.2, size=(dimensions, 1))
        for i in range(dimensions):
            self.velocity[i] = float("{0:.10f}".format(float(self.velocity[i])))
        self.pbest = self.position

    def updateVelocities(self, gbest, w, dimensions):
        for i in range(dimensions):
            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)
            social = c1 * r1 * (gbest[i] - self.position[i])
            cognitive = c2 * r2 * (self.pbest[i] - self.position[i])
            self.velocity[i] = (w * self.velocity[i]) + social + cognitive
            for i in range(dimensions):
                self.velocity[i] = float("{0:.10f}".format(float(self.velocity[i])))

    def updatePosition(self, dimensions):
        for i in range(dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            if (self.position[i] > 10 or self.position[i] < -10):
                for i in range(dimensions):
                    self.position[i] = np.random.uniform(-10, 10)
                break
            self.position[i] = float("{0:.10f}".format(float(self.position[i])))


def func(points):
    y = Ackley(points)
    return y


def main():
    solution = []
    swarm = []

    w = 0.9
    w_mod = (0.5) / max_nfc

    runs = 5
    run = 0
    allruns = []
    allrunsmax = []
    allrunsmean = []
    allrunsstd = []

    print("Initializing " + str(size) + " particles...")
    for i in range(0, size):
        particle = Particle(dimensions)
        swarm.append(particle)

    print("Iterating " + str(max_nfc) + " times...")
    gbest = swarm[0].position
    while (run < runs):
        rundata = []
        rundatamax=[]
        rundatamean = []
        rundatastd = []
        nfc=0
        for i in range(max_nfc):
            pointlist = []
            if (i % 100 == 0 and i > 0):
                print("Iterating: " + str(i) + "/" + str(max_nfc))
                '''
                print("X1: " + str(solution[0]))
                print("X2: " + str(solution[1]))
                '''
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
                print("Current Solution: " + str(func(solution)))
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

            if nfc%100 == 0:
                rundata.append(min(func(pointlist)))
                rundatamax.append(max(func(pointlist)))
                rundatamean.append(np.mean(func(pointlist)))
                rundatastd.append(np.std(func(pointlist)))
        print rundata
        print rundatamax
        print rundatamean
        print rundatastd
        print "rundata above"
        run = run + 1
        if run%10==0:
            print('On run: ',run)
    allruns.append(rundata)
    allrunsmax.append(rundatamax)
    allrunsmean.append(rundatamean)
    allrunsstd.append(rundatastd)
    allruns = np.asarray(allruns)
    allruns = np.reshape(allruns, (runs, max_nfc / size))
    final_runmin = allruns[:, -1]
    final_runmax = allrunsmax[:, -1]
    final_runmean = allrunsmean[:, -1]
    final_runstd = allrunsstd[:, -1]
    plot_runs = np.average(allruns, axis=0)  # This is for the plots
    print final_runmin
    print final_runmax
    print final_runmean
    print final_runstd
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



main()
