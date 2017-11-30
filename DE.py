import numpy as np
from Functions import *


class population(object):

    def __init__(self, dimensions, nump=100):

        self.nump = nump
        self.dimensions = dimensions
        self.nump = nump
        self.rangep = {'max':10, 'min':-10}
        self.points = np.random.uniform(self.rangep['min'],self.rangep['max'],size=(self.dimensions,self.nump))

    def setpoints(self,points):
        self.points = points

    def randselect(self):
        X = np.random.choice(range(0,self.nump-1), size=3 , replace=False)
        return X

    def mutation(self):
        F = 0.8
        v = self.points[:,self.randselect()[0]] + F * (self.points[:,self.randselect()[2]] - self.points[:,self.randselect()[1]])
        return v

    def crossover(self,mutatedvec,pointno):
        Cr = 0.9
        self.trialvec = np.empty([self.dimensions,1])
        for j in range(0,self.dimensions):
            if np.random.rand() < Cr:
                self.trialvec[j] = mutatedvec[j]
            else:
                self.trialvec[j] = self.points[j,pointno]
        return self.trialvec

    def get_points(self):
        return self.points



def optimize(dim,func):
    #Parameters
    dimnesions = dim
    pop = 100
    max_nfc=300*dimnesions
    runs = 3
    run=0
    allruns = []
    allrunsmax=[]
    allrunsmean=[]
    allrunsstd = []
    nodes = population(dimnesions,pop)
    while (run < runs):
        rundata = []
        rundatamax=[]
        rundatamean = []
        rundatastd = []
        nfc=0
        while( nfc < max_nfc):
            newnodes = np.empty([dimnesions,pop])
            for i in range(0,pop):
                trialvec = nodes.crossover(nodes.mutation(),i)
                if func(trialvec)<=func(nodes.get_points()[:,i]):
                    newnodes[:,i] = trialvec.reshape(dimnesions)
                else:
                    newnodes[:,i] = nodes.get_points()[:,i]
            nodes.setpoints(newnodes)
            if nfc%pop == 0:
                rundata.append(min(func(nodes.get_points())))
                rundatamax.append(max(func(nodes.get_points())))
                rundatamean.append(np.mean(func(nodes.get_points())))
                rundatastd.append(np.std(func(nodes.get_points())))
            nfc = nfc + 1
        run = run+1
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
    allruns = np.reshape(allruns,(runs,max_nfc/pop) )
    allrunsmax = np.reshape(allrunsmax,(runs,max_nfc/pop) )
    allrunsmean = np.reshape(allrunsmean,(runs,max_nfc/pop) )
    allrunsstd = np.reshape(allrunsstd,(runs,max_nfc/pop) )
    final_runmin =allruns[:,-1]
    final_runmax =allrunsmax[:,-1]
    final_runmean =allrunsmean[:,-1]
    final_runstd =allrunsstd[:,-1]
    plot_runs = np.average(allruns,axis=0) # This is for the plots

    return plot_runs, final_runmin,final_runmax,final_runmean,final_runstd



