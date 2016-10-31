#CSE 461 Labs

---

##LAB 1:

Write a program that implements the following disk-scheduling algorithms:
 * a. FCFS - first come first serve
 * b. SSTF - sortest path to next head movement
 * c. SCAN - scan to zero and then back up - given start head location
 * d. C-SCAN - scan to end of disk then back down - given start head location
 * e. LOOK 
 * f. C-LOOK 

Your program will service a disk with 5,000 cylinders numbered 0 to 4,999. The program will generate a random 
series of 1,000 cylinder requests and service them according to each of the algorithms listed above. The 
program will be passed the initial position of the disk head (as a parameter on the command line) and report 
the total amount of head movement required by each algorithm.

###HOW TO TURN IN
Source Code, Screenshot of Executed Code, Results and Strategy used to approach solution. 

---

##LAB 2:

You should be able to change all these parameters to define a different disk

```
cylinders = 4096 
block_size = 512
blocks_per_track = 64  // (64 blocks per track on 4 platters with 8 heads, same as 8 tracks)
blocks_per_cylnder = blocks_track * number_tracks
bytes_per_cylinder = blocks_per_cylinder*bytes_per_block
8 tracks per cylinder = 512*8 // this is minimum bytes read - 1 block * 8 tracks = 4K
//  4K tracks * 64 512 byte blocks/track * 8 tracks/cylinder => 1T bytes
//  we have 4K * 64 addresses = 262144

address space: 262144 (0 to 262143), with each address pointing at 4K

avg_seek_time = 10 ms // 10*1e-3 , average time to move head to a given cylinder
rotation_speed = 7200 rpm // average rot_latency = 4.2 ms = 4.2*e^-3 sec ~ 1/2 rotation

// maximum bandwidth is :
// bytes_per_cylinder/(time-of-rotation-in-sec): in bytes/second

page_size =  // you decide, page is usually 4K-16K

```
pages are numbered MAX-1, where MAX is number_blocks/blocks_per_page 

Assume a first-come, first-served strategy:

 * A) Given: list of 100 pages, randomly generated
	calculate - time to read all requests, 
	effective bandwidth (total bytes read)/(time to read requests)

note: read first page = seek+rot_latency+bytes/max_bandwidth

	time to read next page : assume you always have rotational latency, but
	add seek time only if have to change cylinders.
	  
 * B) Consider multi-page requests : i.e. if a program requests N consecutive pages,
rot. latency can be ignored unless request is on more than one cylinder. If it does, switching cylinders incurs seek and rotation.

Do multipage requests affect effective bandwidth?

---

NOTE:
 * Cylinder - The set of tracks that are at one arm position makes up a cylinder.
 * Seek Time - the time necessary to move the disk arm to the desired cylinder.
 * Rotational Latency - the time necessary for the desired sector to rotate to the disk head.
 * Mapping - The mapping proceeds in order through that track, then through the rest of the tracks in that cylinder, and then through the rest of the cylinders from outermost to innermost

---


    

