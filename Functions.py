import numpy as np
import math



def highCond(dim):
    firstSum = 0
    for count, c in enumerate(dim):
        count += 1
        firstSum += np.power((10 ** 6), ((count - 1)/(len(dim) - 1))) * np.power(c, 2)
    return firstSum


def bentCig(dim):
    firstSum = 0
    for c in dim[1:]:
        firstSum += np.power(c, 2)
    return np.power(dim[0], 2) + (10 ** 6) * firstSum


def discus(dim):
    firstSum = 0
    for c in dim[1:]:
        firstSum += np.power(c, 2)
    return (10 ** 6) * np.power(dim[0], 2) + firstSum


def rosen(dim):
    firstSum = 0
    dim2 = dim[:-1]
    for count, c in enumerate(dim2):
        firstSum = (100 * np.power((np.power(c, 2) - dim[count + 1]), 2) + np.power((c - 1), 2))
        count += 1
    return firstSum


def Ackley(dim):
    firstSum = 0.0
    secondSum = 0.0
    for c in dim:
        firstSum += c ** 2.0
        secondSum += np.cos(2.0 * math.pi * c)
    n = float(len(dim))
    return -20.0 * np.exp(-0.2 * np.sqrt(firstSum / n)) - np.exp(secondSum / n) + 20 + math.e


# Weierstrass
def innersum(dim):


    kmax = 20
    a = 0.5
    b = 3
    sum1 = 0
    pi2 = 2*math.pi
    dim5 = dim+0.5
    k = range(0,kmax)
    aa = np.power(a,k)
    bb = np.power(b,k)
    for k in range(0, kmax):
        sum1 += (aa[k] * np.cos(pi2 * bb[k] * dim5))
    return sum1





def insum(dim):
    firstSum = 0

    for j in range(1, 32):
        powe = np.power(2, j)
        firstSum += ((powe * dim - np.round(powe * dim)) / powe)
    return firstSum


def innersum2():
    kmax = 20
    a = 0.5
    b = 3
    sum1 = 0
    pi2 = 2*math.pi
    for k in range(0, kmax):
        sum1 += (np.power(a, k) * np.cos(pi2 * np.power(b, k) * 0.5))
    return sum1


def weirerstrass(dim):
    firstSum = 0
    secondSum = 0
    for c in dim:
        firstSum += innersum(c)
        secondSum += innersum2()
    return firstSum - len(dim) * secondSum


def griewank(dim):
    firstSum = 0
    firstProd = 0
    for count, c in enumerate(dim):
        count += 1
        firstSum += (np.power(c, 2) / 4000)
        firstProd *= (np.cos(c / np.sqrt(count)))
    return firstSum - firstProd + 1


def rastrigin(dim):
    firstSum = 0
    for c in dim:
        firstSum += (np.power(c, 2) - 10 * np.cos(2 * math.pi * c) + 10)
    return firstSum


def katsuura(dim):
    firstProd = 10

    dividor = 10 / np.power(len(dim), 1.2)
    for count, c in enumerate(dim):
        count += 1
        firstProd *= np.power((1 + count * insum(c)),dividor)
    return (10 / np.power(len(dim), 2)) * firstProd - (10 / np.power(len(dim), 2))