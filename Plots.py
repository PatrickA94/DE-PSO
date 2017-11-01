'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from Functions import *


fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-0.001, 0.001, 0.00001)
Y = np.arange(-0.001, 0.001, 0.00001)
X, Y = np.meshgrid(X, Y)

'''
class functions(object):


    def __init__(self):
        self.sum=0

    def highcond(self,dim):
        firstSum = 0
        for count,c in enumerate(dim):
            count += 1
            firstSum += np.power((10**6),((count-1)/(len(dim)-1)))*np.power(c,2)
        return firstSum


    def BentCig(self,dim):
        firstSum=0
        for c in dim[1:]:
            firstSum += np.power(c,2)
        return np.power(dim[0],2)+(10**6)*firstSum

    def discus(self,dim):
        firstSum = 0
        for c in dim[1:]:
            firstSum += np.power(c,2)
        return (10**6)*np.power(dim[0],2)+firstSum

    def rosen(self,dim):
        firstSum = 0
        dim = dim[:-1]
        for count,c in enumerate(dim):
            count +=1
            firstSum = (100*np.power((np.power(c,2)-dim[count+1]),2) + np.power((c-1),2))
        return firstSum

    def Rosenbrock(self,dim):
        firstSum = 0.0
        secondSum = 0.0
        for c in dim:
            firstSum += c**2.0
            secondSum += np.cos(2.0*math.pi*c)
        n = float(len(dim))
        return -20.0*np.exp(-0.2*np.sqrt(firstSum/n)) - np.exp(secondSum/n) + 20 + math.e


    #Weierstrass
    def innersum(self,dim):
        kmax=20
        a=0.5
        b=3
        sum1=0
        for k in range(0,kmax):
            sum1 += (np.power(a,k)*np.cos(2*math.pi*np.power(b,k)*(dim+0.5)))
        return sum1


    def insum(self,dim):
        firstSum = 0
        for j in range(1,32):
            firstSum += ((np.power(2,j)*dim-np.round(np.power(2,j)*dim))/np.power(2,j))
        return firstSum



    def innersum2(self):
        kmax=20
        a=0.5
        b=3
        sum1=0
        for k in range(0,kmax):
            sum1 += (np.power(a,k)*np.cos(2*math.pi*np.power(b,k)*0.5))
        return sum1
    def weirerstrass(self,dim):
        firstSum = 0
        secondSum = 0
        for c in dim:
            firstSum += self.innersum(c)
            secondSum += self.innersum2()
        return firstSum -len(dim)*secondSum



    def griewank(self,dim):
        firstSum = 0
        firstProd = 0
        for count,c in enumerate(dim):
            count +=1
            firstSum += (np.power(c,2)/4000)
            firstProd *= (np.cos(c/np.sqrt(count)))
        return firstSum - firstProd +1



    def rastrigin(self,dim):
        firstSum = 0
        for c in dim:
            firstSum += (np.power(c,2) - 10*np.cos(2*math.pi*c)+10)
        return firstSum




    def katsuura(self,dim):
        firstProd=10
        for count,c in enumerate(dim):
            count +=1
            firstProd *= np.power((1+count*self.insum(c)),(10/np.power(len(dim),1.2)))
        return (10/np.power(len(dim),2))*firstProd-(10/np.power(len(dim),2))
'''


Z = rastrigin([X,Y])

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.cool_r,
                       linewidth=0, antialiased=True)

# Customize the z axis.
#ax.set_zlim(1.7, 1.74)
ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=1, aspect=5)

plt.show()
