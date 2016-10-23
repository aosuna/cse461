# Write a program that implements the following disk-scheduling algorithms:
# a.X FCFS -fifo
# b.X SSTF - sortest path to next head movement
# c.X SCAN - scan to zero and then back up - given start head location
# d.X C-SCAN - scan to end of disk then back down - given start head location
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

#print out the average head movement for each algorithm, store each run in a temp
FCFSheadMov = []
SSTFheadMov = []
SCANheadMov = []
C_SCANheadMov = []


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
	resultArry = list(scheduling)
	minDistArry = []
	j = 1
	resultArry.insert(0, startHead)
	for x in xrange(len(resultArry) - 1):
			headMov = abs( resultArry[x] - resultArry[x+1] )
			minDistArry.append(headMov)

	FCFSheadMov.append(sum(minDistArry))

#Shortest Seek Time First Algorithm
def SSTF(scheduling, headPos):
	resultArry = list(scheduling)
	minDistArry = []
	while(len(resultArry) > 1):
		minDist = 0
		minDist = abs(resultArry[0] - headPos)	
		arryElmt = resultArry[0]
		for x in resultArry:
			if(abs(headPos - x) < minDist):
				minDist = abs(headPos - x)
				arryElmt = x
		minDistArry.append(minDist)
		resultArry.remove(arryElmt)
		headPos = arryElmt

	SSTFheadMov.append(sum(minDistArry))

#SCAN AKA Elevator algorithm
def SCAN(scheduling, headPos):
	resultArry = list(scheduling)
	distArry = []
	dist = 0
	resultArry.append(headPos)
	resultArry = sorted(resultArry)
	startPos = resultArry.index(headPos)
	distArry.append(resultArry[0])

	if(resultArry[startPos] == resultArry[0]):
		for x in xrange(len(resultArry[:])-1):
			dist = abs(resultArry[x] - resultArry[x+1])
			distArry.append(dist)
	elif(resultArry[startPos] == resultArry[len(resultArry)-1]):
		resultArry.reverse()
		for x in xrange(len(resultArry) -1):
			if(x == 1):
				dist = abs(cylinder - resultArry[x])
				distArry.append(dist)
	else:
		for x in xrange(len(resultArry[:startPos]) - 1):
			dist = abs(resultArry[x] - resultArry[x+1])
			distArry.append(dist)
		resultArry.reverse()
		for x in xrange(len(resultArry[:startPos]) - 1):
			if(x == startPos):
				distArry.append(resultArry[x-1])
			else:
				dist = abs(resultArry[x] - resultArry[x+1])
				distArry.append(dist)

	SCANheadMov.append(sum(distArry))

#C-SCAN
def C_SCAN(scheduling, headPos):
	resultArry = list(scheduling)
	distArry = []
	dist = 0
	resultArry.append(headPos)
	resultArry.append(0)
	resultArry.append(cylinder)
	resultArry = sorted(resultArry)
	startPos = resultArry.index(headPos)
	
	#if start postion is the first in the list
	if(resultArry[startPos] == resultArry[0]):
		for x in xrange(len(resultArry[:])-1):
			dist = abs(resultArry[x] - resultArry[x+1])
			distArry.append(dist)
	#if number to the left of start postion holds the sortest distance
	elif(abs(resultArry[startPos] - resultArry[startPos-1]) < abs(resultArry[startPos] - resultArry[startPos+1])):
		for x in xrange(len(resultArry[:startPos]) -1):
			if(x == 0):
				distArry.append(resultArry[0])
			dist = abs(resultArry[x] - resultArry[x+1])
			distArry.append(dist)

		for x in xrange(len(scheduling[startPos+1:]) -1): #need to iterate only upto to the number before previous head position
			dist = abs(scheduling[x] - scheduling[x+1])
			distArry.append(dist)
	#if number to the right of start position hold sortest distance
	else:
		for x in xrange(len(scheduling[startPos:]) - 1):
			if(x == len(scheduling) - 1):
				dist = abs(scheduling[x] - cylinder)
				distArry.append(dist)
			else:
				dist = abs(scheduling[x] - scheduling[x+1])
				distArry.append(dist)
		for x in xrange(len(scheduling[:startPos]) - 2):
			dist = abs(scheduling[x] - scheduling[x+1])
			distArry.append(dist)

	C_SCANheadMov.append(sum(distArry))

#Main function
if __name__ == "__main__":
	i = 1
	while (i < 11):
		diskSchedule = getSchedule()
		FCFS(diskSchedule)
		SSTF(diskSchedule, startHead)
		SCAN(diskSchedule, startHead)
		C_SCAN(diskSchedule, startHead)
		i += 1

	print "First come first serve ", numpy.mean(FCFSheadMov)
	print "Sortest seek time first ", numpy.mean(SSTFheadMov)
	print "Scan ", numpy.mean(SCANheadMov)
	print "C-Scan ", numpy.mean(C_SCANheadMov)

