# Write a program that implements the following disk-scheduling algorithms:
# a.X FCFS -fifo
# b.X SSTF - sortest path to next head movement
# c.X SCAN - scan to zero and then back up - given start head location
# d. C-SCAN - scan to end of disk then back down - given start head location
# e. LOOK - 
# f. C-LOOK - 
# Your program will service a disk with 5,000 cylinders numbered 0 to 4,999. The program will generate a random 
# series of 1,000 cylinder requests and service them according to each of the algorithms listed above. The 
# program will be passed the initial position of the disk head (as a parameter on the command line) and report 
# the total amount of head movement required by each algorithm.

#HOW TO TURN IN
#source code, screenshot of executed code, results, strategy, 

import random
import numpy

i = 0
cylinder = 4999
block = 512
SIZE = 10

testArry = [98,183,37,122,14,128,65,67] 

#print out the average head movement for each algorithm, store each run in a temp
FCFSheadMov = []
SSTFheadMov = []
SCANheadMov = []


startHead = raw_input("Enter the start head position: ")
startHead = int(startHead)

#generates several request for disk access
def getSchedule():
	request = []
	#request.append(startHead)
	while(len(request) < SIZE):
		request.append(random.randint(0,cylinder))
	return request

#First Come First Serve Algorithm 
def FCFS(scheduling):
	minDistArry = []
	j = 1
	scheduling.insert(0, startHead)
	for x in xrange(len(scheduling) - 1):
			headMov = abs( scheduling[x] - scheduling[x+1] )
			minDistArry.append(headMov)

	FCFSheadMov.append(numpy.mean(minDistArry))

#Shortest Seek Time First Algorithm
def SSTF(scheduling, headPos):
	minDistArry = []
	while(len(scheduling) > 1):
		minDist = 0
		minDist = abs(scheduling[0] - headPos)	
		arrElmt = scheduling[0]
		for x in scheduling:
			if( abs(headPos - x) < minDist):
				minDist = abs(headPos - x)
				arrElmt = x
		minDistArry.append(minDist)
		scheduling.remove(arrElmt)

	SSTFheadMov.append(numpy.mean(minDistArry))

#SCAN AKA Elevator algorithm
def SCAN(scheduling, headPos):
	distArry = []
	dist = 0
	scheduling.append(headPos)
	numpy.sort(scheduling)
	startPos = scheduling.index(headPos)
	distArry.append(scheduling[0])
	for x in xrange(len(scheduling[:startPos]) - 1):
		dist = abs(scheduling[x] - scheduling[x+1])
		distArry.append(dist)
	scheduling.reverse()
	for x in xrange(len(scheduling[:startPos]) - 1):
		if(x == startPos):
			distArry.append(scheduling[x-1])
		else:
			dist = abs(scheduling[x] - scheduling[x+1])
			distArry.append(dist)

	SCANheadMov.append(numpy.mean(distArry))

SCAN(testArry, startHead)
print SCANheadMov

''' TEST FOR MAIN 
def main():
	FCFS(testArry)
	SSTF(testArry, startHead)
	print FCFSheadMov
	print SSTFheadMov

if __name__ == '__main__':
	main()
'''