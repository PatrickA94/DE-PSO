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


def func(points):
    y = katsuura(points)
    return y


def main():
    #Parameters
    dimnesions = 2
    pop = 10
    nfc = 0
    max_nfc=30*dimnesions
    runs = 51
    run=0
    allruns = []
    nodes = population(dimnesions,pop)
    while (run < runs):
        run = []
        while( nfc < max_nfc):
            newnodes = np.empty([dimnesions,pop])
            for i in range(0,pop):
                trialvec = nodes.crossover(nodes.mutation(),i)
                if func(trialvec)<=func(nodes.points[:,i]):
                    newnodes[:,i] = trialvec.reshape(dimnesions)
                else:
                    newnodes[:,i] = nodes.points[:,i]
            nodes.setpoints(newnodes)
            nfc = nfc+1
            if nfc%pop == 0:
                run.append(func(nodes.points))
        allruns.append(run)

    allruns = np.asarray(allruns)
    final_run =allruns[:,-1]
    plot_runs = np.average(allruns,axis=1)[0] # This is for the plots

    print final_run
    return plot_runs, final_run



if __name__ == "__main__":
    main()




