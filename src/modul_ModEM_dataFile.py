#!/usr/bin/env python3

import numpy as np

def readModelFile(file):

    opMod = open(file,'r')

    readAllData = opMod.readlines() 

    nY, nX, nZ, temp, typeRes = readAllData[1].split()
    
    nX = int(nX)
    nY = int(nY)
    nZ = int(nZ)

    lX = readAllData[3].split()
    lY = readAllData[2].split()
    lZ = readAllData[4].split()

    lX = list(map(float, lX))
    lY = list(map(float, lY))
    lZ = list(map(float, lZ))
 
    array = np.zeros(shape=(nZ, nY, nX)) 
    
    k=6
    for j in range(nZ):
        for i in range(nX):
            temp = readAllData[k].split()
            temp = list(map(float, temp))

            array[j,i,:] = temp
            k+=1
        k+=1

    array = np.exp(array)

    return nX, nY, nZ, lX, lY, lZ, array

def test(var):
    return var*2

if __name__ == '__main__':

    file = '../data/model.mod'

    nX, nY, nZ, lX, lY, lZ, array = readModelFile(file)
