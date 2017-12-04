import numpy as np
from Functions import *
import cProfile
import random


class population(object):

    def __init__(self, dimensions,func ,nump=100 ):

        self.nump = nump
        self.dimensions = dimensions
        self.nump = nump
        self.rangep = {'max':10, 'min':-10}
        self.points = np.random.uniform(self.rangep['min'],self.rangep['max'],size=(self.dimensions,self.nump))
        self.current_fitness = func(self.points)

    def setpoints(self,points):
        self.points = points

    def randselect(self):
        X =  random.sample(range(0,99),3)
        return X

    def mutation(self):
        F = 0.8
        v = self.points[:,self.randselect()[0]] + F * (self.points[:,self.randselect()[2]] - self.points[:,self.randselect()[1]])
        if any(vin > 10 for vin in v):
            for cnt,vin in enumerate(v):
                if vin >10:
                    v[cnt] = 10
        if any(vin< -10 for vin in v):
            for cnt,vin in enumerate(v):
                if vin >10:
                    v[cnt] = 10
        return v

    def crossover(self,mutatedvec,pointno):
        Cr = 0.9
        self.trialvec = np.empty([self.dimensions,1])
        mutationscnt = 0
        for j in range(0,self.dimensions):
            if np.random.rand() < Cr:
                self.trialvec[j] = mutatedvec[j]
                mutationscnt+=1
            else:
                self.trialvec[j] = self.points[j,pointno]
        if mutationscnt== 0:
            return self.trialvec,True
        else:
            return self.trialvec, False


    def get_points(self):
        return self.points

    def get_node_fitness(self,i):
        return self.current_fitness[i]

    def get_current_fitness(self):
        return self.current_fitness

    def set_current_fitness(self,fitness,i):
        self.current_fitness[i]=fitness



def optimize(dim,func):
    print('Started DE')
    #Parameters
    dimnesions = dim
    pop = 100
    max_nfc=3000*dimnesions
    runs = 5
    run=0
    allruns = []
    allrunsmax=[]
    allrunsmean=[]
    allrunsstd = []
    nodes = population(dimnesions,func,pop)
    while (run < runs):
        rundata = []
        rundatamax=[]
        rundatamean = []
        rundatastd = []
        nfc=0
        while( nfc < max_nfc):
            newnodes = np.empty([dimnesions,pop])



            for i in range(0,pop):
                trialvec,functest = nodes.crossover(nodes.mutation(),i)
                if functest == True:
                    trialvec_fitness = nodes.get_node_fitness(i)
                else:
                    trialvec_fitness = func(trialvec)
                if trialvec_fitness<=nodes.get_node_fitness(i):
                    nodes.set_current_fitness(trialvec_fitness,i)
                    newnodes[:,i] = trialvec.reshape(dimnesions)
                else:
                    newnodes[:,i] = nodes.get_points()[:,i]
            nodes.setpoints(newnodes)
            if nfc%pop == 0:
                rundata.append(min(nodes.get_current_fitness()))
                rundatamax.append(max(nodes.get_current_fitness()))
                rundatamean.append(np.mean(nodes.get_current_fitness()))
                rundatastd.append(np.std(nodes.get_current_fitness()))
            nfc = nfc + 1
        run = run+1
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
    allruns = np.reshape(allruns,(runs,max_nfc/pop) )
    allrunsmax = np.reshape(allrunsmax,(runs,max_nfc/pop) )
    allrunsmean = np.reshape(allrunsmean,(runs,max_nfc/pop) )
    allrunsstd = np.reshape(allrunsstd,(runs,max_nfc/pop) )
    final_runmin =allruns
    final_runmax =allrunsmax
    final_runmean =allrunsmean
    final_runstd =allrunsstd
    plot_runs = np.average(allruns,axis=0) # This is for the plots

    return plot_runs, final_runmin,final_runmax,final_runmean,final_runstd

#cProfile.run('optimize(2, highCond)',sort='tottime')
