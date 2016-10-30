#Adrian Osuna
#CSE 461 - Dr. Gomez
#Lab 1

import random
import numpy

cylinder = 4999
SIZE = 100
block = 512

#generates several request for disk access
def getSchedule():
	request = []
	#request.append(startHead)
	while(len(request) < SIZE):
		request.append(random.randint(0,cylinder))
	return request

class DiskScheduling():
	#print out the average head movement for each algorithm, store each run in a temp

	FCFSheadMov = []
	SSTFheadMov = []
	SCANheadMov = []
	C_SCANheadMov = []
	LOOKheadMov = []
	C_LOOKheadMov = []

	FCFS_pos = -1
	SSTF_pos = -1
	SCAN_pos = -1
	CSCAN_pos = -1
	LOOK_pos = -1
	CLOOK_pos = -1

	def __init__(self,request,start):
		self.request = request
		self.start = start

	#First Come First Serve Algorithm 
	def FCFS(self):
		resultArry = list(self.request)
		minDistArry = []
		startHead = self.start
		if (self.FCFS_pos != -1):
			startHead = self.FCFS_pos
		
		resultArry.insert(0, startHead)
		for x in xrange(len(resultArry)-1):
			dist = abs( resultArry[x] - resultArry[x+1] )
			minDistArry.append(dist)
		self.FCFS_pos = resultArry[-1]

		self.FCFSheadMov.append(sum(minDistArry))

	#Shortest Seek Time First Algorithm
	def SSTF(self):
		resultArry = list(self.request)
		minDistArry = []
		startHead = self.start
		if(self.SSTF_pos != -1):
			startHead = self.SSTF_pos
		while(len(resultArry) > 1):
			minDist = abs(resultArry[0] - startHead)
			arryElmt = resultArry[0]
			for x in resultArry:
				if(abs(startHead - x) < minDist):
					minDist = abs(startHead - x)
					arryElmt = x
			minDistArry.append(minDist)
			resultArry.remove(arryElmt)
			startHead = arryElmt
		self.SSTF_pos = resultArry[-1]

		self.SSTFheadMov.append(sum(minDistArry))

	#SCAN AKA Elevator algorithm
	def SCAN(self):
		resultArry = list(self.request)
		distArry = []
		dist = 0
		startHead = self.start
		if(self.SCAN_pos != -1):
			startHead = self.SCAN_pos
		resultArry.append(startHead)
		resultArry = sorted(resultArry)
		startPos = resultArry.index(startHead)

		#if the start position is the beginning
		if(resultArry[startPos] == resultArry[0]):
			if(resultArry[0] == 0):
				distArry.append(abs(resultArry[0] - resultArry[-1]))
			for x in xrange(len(resultArry)-1,1,-1):
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			self.SCAN_pos = resultArry[1]

		#if the start position is at the end
		elif(resultArry[startPos] == resultArry[-1]):
			#iterate through the array in reverse
			for x in xrange(len(resultArry)-1,0,-1):
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			self.SCAN_pos = resultArry[0]
		#start position is not at the end or at the beginning
		else:
			#go through the right side first
			for x in xrange(startPos,len(resultArry)-1):
				dist = abs(resultArry[x] - resultArry[x+1])
				distArry.append(dist)
			#go through the left side second
			for x in xrange(startPos-1,0,-1):
					dist = abs(resultArry[x] - resultArry[x-1])
					distArry.append(dist)
			self.SCAN_pos = resultArry[0]

		self.SCANheadMov.append(sum(distArry))

	#C-SCAN
	def C_SCAN(self):
		resultArry = list(self.request)
		distArry = []
		dist = 0
		startHead = self.start
		if(self.CSCAN_pos != -1):
			startHead = self.CSCAN_pos
		resultArry.append(startHead)
		resultArry = sorted(resultArry)
		startPos = resultArry.index(startHead)
		
		#if start postion is the first in the list
		if(resultArry[startPos] == resultArry[0]):
			for x in xrange(len(resultArry)-1):
				dist = abs(resultArry[x] - resultArry[x+1])
				distArry.append(dist)
			self.CSCAN_pos = resultArry[-1]

		#if number to the left of start postion holds the sortest distance
		elif(abs(resultArry[startPos] - resultArry[startPos-1]) < abs(resultArry[startPos] - resultArry[startPos+1])):
			for x in xrange(startPos,0,-1):
				if(x == 0):
					distArry.append(resultArry[0]) #distance from zero first element
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			for x in xrange(startPos+1,len(resultArry)-1): #from start +1 to end
				if(x == startPos+1):
					distArry.append(resultArry[x]) #distance from zero to rest of array
				dist = abs(resultArry[x] - resultArry[x+1])
				distArry.append(dist)
			self.CSCAN_pos = resultArry[-1]
		#if number to the right of start position hold sortest distance
		else:
			for x in xrange(startPos,len(resultArry)-1):
				if(x == len(resultArry)-1): #at end of list to end of disk
					dist = abs(resultArry[x] - cylinder) 
					distArry.append(dist)
				dist = abs(resultArry[x] - resultArry[x+1])
				distArry.append(dist)
			for x in xrange(startPos-1,0,-1):
				if(x == startPos-1):
					dist = abs(cylinder - resultArry[x])
					distArry.append(dist)
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			self.CSCAN_pos = resultArry[0]
		self.C_SCANheadMov.append(sum(distArry))

	def LOOK(self):
		resultArry = list(self.request)
		distArry = []
		dist = 0
		startHead = self.start
		if(self.LOOK_pos != -1):
			startHead = self.LOOK_pos
		resultArry.append(startHead)
		resultArry = sorted(resultArry)
		startPos = resultArry.index(startHead)

		if(resultArry[startPos] == resultArry[-1]):
			for x in xrange(len(resultArry),0, -1):
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			self.LOOK_pos = resultArry[0]
		else:
			#left value is greater than right value
			if(abs(resultArry[startPos] - resultArry[startPos+1]) < abs(resultArry[startPos] - resultArry[startPos-1])):
				#go through right half of the array
				for x in xrange(startPos,len(resultArry)-1):
					dist = abs(resultArry[x] - resultArry[x+1])
					distArry.append(dist)
				#if the start was not at beginning go through the left side of array
				for x in xrange(startPos-1,0,-1):
					if(x == startPos-1): #take distance from the end of list to the one previous to the OG start position
						dist = abs(resultArry[-1] - resultArry[x])
						distArry.append(dist)
					dist = abs(resultArry[x] - resultArry[x-1])
					distArry.append(dist)
				self.LOOK_pos = resultArry[0]
			#right value is greater than left value
			else:
				for x in xrange(startPos,0,-1):
					dist = abs(resultArry[x] - resultArry[x-1])
					distArry.append(dist)

				for x in xrange(startPos+1,len(resultArry)-1):
					if(x == startPos+1):
						dist = abs(resultArry[x] - resultArry[0])
					dist = abs(resultArry[x] - resultArry[x+1])
					distArry.append(dist)
				self.LOOK_pos = resultArry[-1]

		self.LOOKheadMov.append(sum(distArry))

	def C_LOOK(self):
		resultArry = list(self.request)
		distArry = []
		dist = 0
		startHead = self.start
		if(self.CLOOK_pos != -1):
			startHead = self.CLOOK_pos
		resultArry.append(startHead)
		resultArry = sorted(resultArry)
		startPos = resultArry.index(startHead)

		if(startPos == len(resultArry)-1):
			for x in xrange(len(resultArry)-1,0, -1):
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			self.CLOOK_pos = resultArry[0]
		elif(resultArry[startPos] == resultArry[0]):
			for x in xrange(0,len(resultArry)-1):
				dist = abs(resultArry[x] - resultArry[x-1])
				distArry.append(dist)
			self.CLOOK_pos = resultArry[-1]
		else:
			#left value is greater than right value
			if(abs(resultArry[startPos] - resultArry[startPos+1]) < abs(resultArry[startPos] - resultArry[startPos-1])):
				#go through right half of the array
				for x in xrange(startPos,len(resultArry)-1):
					dist = abs(resultArry[x] - resultArry[x+1])
					distArry.append(dist)
				#if the start was not at beginning go through the left side of array
				for x in xrange(startPos-1,0,-1):
					if(x == startPos -1):
						dist = abs(resultArry[x] - resultArry[-1])
						distArry.append(dist)
					dist = abs(resultArry[x] - resultArry[x-1])
					distArry.append(dist)
				self.CLOOK_pos = resultArry[0]
			#right value is greater than left value
			else:
				for x in xrange(startPos, 0, -1):
					dist = abs(resultArry[x] - resultArry[x-1])
					distArry.append(dist)
				for x in xrange(startPos+1,len(resultArry)-1):
					if(x == startPos+1):
						dist = abs(resultArry[x] - resultArry[0])
						distArry.append(dist)
					dist = abs(resultArry[x] - resultArry[x+1])
					distArry.append(dist)
				self.CLOOK_pos = resultArry[-1]

		self.C_LOOKheadMov.append(sum(distArry))

#Main function
if __name__ == "__main__":
	fcfsSTD = []
	sstfSTD = []
	scanSTD = []
	cscanSTD = []
	lookSTD = []
	clookSTD = []
	startHead = int(input("Enter the start head position a value from 0 - 4999: "))
	if(startHead < 4999 and startHead > 0):
		for j in xrange(5):
			for i in xrange(10):
				request = getSchedule()
				disk = DiskScheduling(request, startHead)

				disk.FCFS()
				disk.SSTF()
				disk.SCAN()
				disk.C_SCAN()
				disk.LOOK()
				disk.C_LOOK()

			print "List ", j
			print "FCFS: ", (sum(disk.FCFSheadMov) / 1000)
			print "SSTF: ", (sum(disk.SSTFheadMov) / 1000)
			print "Scan: ", (sum(disk.SCANheadMov) / 1000)
			print "C-Scan: ", (sum(disk.C_SCANheadMov) / 1000)
			print "Look: ", (sum(disk.LOOKheadMov) / 1000)
			print "C-Look: ", (sum(disk.C_LOOKheadMov) / 1000)
			print "\n"


			fcfsSTD.append(sum(disk.FCFSheadMov) / 1000)
			sstfSTD.append(sum(disk.SSTFheadMov) / 1000)
			scanSTD.append(sum(disk.SCANheadMov) / 1000)
			cscanSTD.append(sum(disk.C_SCANheadMov) / 1000)
			lookSTD.append(sum(disk.LOOKheadMov) / 1000)
			clookSTD.append(sum(disk.C_LOOKheadMov) / 1000)

		print "FCFS Standard Deviation: ", numpy.std(fcfsSTD)
		print "SSTF Standard Deviation: ", numpy.std(sstfSTD)
		print "SCAN Standard Deviation: ", numpy.std(scanSTD)
		print "C-SCAN Standard Deviation: ", numpy.std(cscanSTD)
		print "LOOK Standard Deviation: ", numpy.std(lookSTD)
		print "C-LOOK Standard Deviation: ", numpy.std(clookSTD)
	else:
		print "Invalid input \n"
