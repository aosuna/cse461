#Adrian Osuna
#CSE 461 - Dr. Gomez
#Lab 2
# -*- coding: utf-8 -*-

import random
import numpy

cylinders = 4096
block_size = 512 #also the bytes per block
number_tracks_per_cylinder = 8
blocks_per_track = 64
blocks_per_cylinder = blocks_per_track * number_tracks_per_cylinder #size equal to 4096
bytes_per_cylinder = blocks_per_cylinder * block_size #size equal to 4096
addresses = blocks_per_cylinder * blocks_per_track - 1#total address avaiable equal to 262143
avg_seek_time = 0.01
average_rotational_latency = 0.0042 # 1/2 rotational latency
max_bandwidth = bytes_per_cylinder / average_rotational_latency
page_size = 4096 #set page size to 4K
MAX = (blocks_per_cylinder / blocks_per_track) - 1 #number of max pages equals 64 pages each page is 4k bytes
												   #to find address on disk, take page number * 4k

prev_page = -1

def getSchedule():
	request = []
	#request.append(startHead)
	while(len(request) < 100):
		request.append(random.randint(0,addresses))
	return request

def FCFS_DiskLatency(request):
	total_seek_time = 0
	prev_page = request[0] // 64 #first page number
	total_seek_time = total_seek_time + avg_seek_time + average_rotational_latency + (request[0]) / max_bandwidth
	for x in xrange(1,len(request) -1):
		curr_page = request[x] // 64 #current page number
		if(prev_page == curr_page):
			total_seek_time = total_seek_time + average_rotational_latency
			prev_page = curr_page
		else:
			total_seek_time = total_seek_time + average_rotational_latency + avg_seek_time
			prev_page = curr_page

	return total_seek_time

if __name__ == '__main__':
	request = getSchedule()
	total_seek_time = FCFS_DiskLatency(request)
	print "Total time to read 100 request: %f" %total_seek_time
