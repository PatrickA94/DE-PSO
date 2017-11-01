import numpy as np

class population(object):



    def __init__(self, dimensions, nump=10):

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
        #print("OG Vector ", self.points[:,pointno])
        #print("Mutated vector ", mutatedvec)
        return self.trialvec


def func(points):
    dimensions = len(points)
    cost=0
    for i in range(1,dimensions):
        y = np.power(10**6,((i-1)/(dimensions-1)))*np.power(points[i],2)
        cost = cost + y
    return cost

def main():
    #Parameters
    dimnesions = 2
    pop = 5
    nfc = 0
    max_nfc=5000*dimnesions



    nodes = population(dimnesions,pop)
    while( nfc < max_nfc):
        newnodes = np.empty([dimnesions,pop])
        for i in range(0,pop):
            trialvec = nodes.crossover(nodes.mutation(),i)
            if func(trialvec)<=func(nodes.points[:,i]):
                newnodes[:,i] = trialvec.reshape(2)
            else:
                newnodes[:,i] = nodes.points[:,i]
        nodes.setpoints(newnodes)
        nfc = nfc+1
    print func(nodes.points)




main()




