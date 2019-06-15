import numpy as np

def readDimension(file):
	temp = file.readline().split()
	temp = [float(i) for i in temp] #convert a list containing string  to float

	return temp

def readBody(file):
	temp = file.readline().split()
	temp = [round(np.exp(float(i)), 2) for i in temp] #convert a list containing string to float, exponent, roundup

	return temp

def readFile(file):
	temp = file.readline() #read 1st line
	temp = file.readline() #read 2nd line - ignore it, will define using len
	
	x = readDimension(file) #read 3rd line
	y = readDimension(file) #read 4th line
	z = readDimension(file) #read 5th line

	# myarray = np.asarray(mylist)
	res = []
	
	temp = file.readline()
	for i in range(len(x)):
		temp = readBody(file)
		print(temp)
	


	return x, y, z

if __name__ == '__main__':

	file = open('../data/model.mod','r')
	x, y, z = readFile(file)

