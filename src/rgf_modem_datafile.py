#!/usr/bin/env python3
'''
rgf_ModEM_dataFile as a part of module from RifLab Geophysical Framework (RGF)

This file is created for read/write files in ModEM data format. Futher information about
ModEM see at http://www.modem-geophysics.com.

author: arif.darmawan@riflab.com

'''
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

if __name__ == '__main__':

    file = '../data/model.mod'

    nX, nY, nZ, lX, lY, lZ, array = readModelFile(file)
