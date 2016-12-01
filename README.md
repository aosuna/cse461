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
	time to read next page| assume you always have rotational latency, but
	add seek time only if have to change cylinders.
	  
 * B) Consider multi-page requests : i.e. if a program requests N consecutive pages, rot. 
      latency can be ignored unless request is on more than one cylinder. If it does, switching 
      cylinders incurs seek and rotation.

Do multipage requests affect effective bandwidth?

---

NOTE:
 * Cylinder - The set of tracks that are at one arm position makes up a cylinder.
 * Seek Time - the time necessary to move the disk arm to the desired cylinder.
 * Rotational Latency - the time necessary for the desired sector to rotate to the disk head.
 * Mapping - The mapping proceeds in order through that track, then through the rest of the tracks in that cylinder, and then through the rest of the cylinders from outermost to innermost

---

##Lab 3:

Investigation of data structures for disk access

 * 1) Input data a randomly generated array of 10,000 strings 
 (in C++ I use the function drand48() to give a double precision number between 0 and 1 then 
  ```
    int C,range,base; // must initialize range and base
    C = drand42() * range + base;
  ```
  gives an integer between base and range+base - for example base=97 range=25 returns the
  ASCII codes fro 'a' to 'z' and you can use this to generate characters in a string of 
  whatever length you want. Then do it 10,000 times to generate your list. There are many
  other ways of doing this, depending on your language of choice).

 * 2) Test 3 different data structures for access time
   specifically how long it takes to find a string in the data, or to verify that a string is not there
   Of the 3 data structures suggested to store a directory, which is fastest? Is the
   speedup sufficient to justify its use? Explain.
    
    * an array of random strings
    * a sorted array of random strings (so you can do binary search)
    * a hash table of the strings (note - hash table should be at least 1.5 times bigger than your list.
   
 * 3) Here is a sample function (in C/C++) that returns system time
 
 
```
#include time.h

/* compile with -lrt option to gcc */

double milisecond_timer(){
struct timespec itval;
/* returns system time in miliseconds */

	clock_gettime(CLOCK_REALTIME,&itval);
	return itval.tv_sec*1000+itval.tv_nsec/1e6;
}
```
For details on system call use: man clock_gettime. Although the system clock is theoretically
running at gigahertz speeds, you can only read it to microseconds with standard calls. This
code divides by 1e6 for seconds, I multiply by 1000 to get miliseconds because measurements close to
the limit are less accurate. You will need to repeat the measurent multiple times in a loop, then
divide by number of iterations.

---

##Lab4:

Determination of usable memory bandwidth:

Memory specifications include latency and bandwidth: for example for DDR2 or DDR3 memory,
the advertised speed (for example: f=1600 GHz) indicates the transfer rate for today's 
standard 64 bit wide memory bus: in bits/sec this is 64xf = 64 * 1.6e9 ; divide by 8 for
bytes/second. This is maximum burst rate, under ideal conditions, ignoring startup time
(latency, a harder to determine value usually somewhere between 10-20 nanoseconds for 
current chips).

What we want to know is how much you can get in fact. You can do this by measuring the time
it takes to move some chunk of memory - you can do this using the memmove function
(see man memmove) or by declaring two arrays and copying from one to the other using a loop.
Note that the iterations you will need depends on what your array is - an array of double
has 8 byte items, an array of int has 4 byte items, so double will require fewer iterations
and probably run faster.

(You may also use memmove in a loop, and copy the array in chunks - I am not sure how much
memory memmove can handle at one time, it might be smaller than your array). 

You should make sure your arrays are too big to fit in cache, or you will actally be measuring
cache speed (modern cache is usually 1 or 2 megabytes per CPU core, in Linux you can get the
cache size by typing "cat /proc/cpuinfo" at the command line). 

You will need to measure time inside the program, sing one of the system timers. A sample
program (in C, but won't need much change to work in C++) is at :

http://www.cse.csusb.edu/egomez/PC/files/timer.c

What you do is, call the timer and save its value before your memory copy operation, then
call the timer again afterwards and subtract the start time. This will give you time to copy
in microseconds (plus whatever overhead you get from the loop or from memmove, which should
be small enough to ignore).

It may be necessary to put your copy action inside another loop that repeats it some
specified N times, then you time the outer loop as above and divide by N to get the copy time.
You may not need this, but depending on array size and computer speed it may give you more
accuracy.

In any case, repeat your measurement multiple times, give an average and standard deviation.

You will need to program in some compiled laguage - in practice this means C or C++ (or assembler
or Fortran, or stranger things). If your are using GNU C or C++ (standard in every Linux 
system) compile with -O3 flag - for example: gcc -O3 memtest.c -o memtest (be sure to add whatever
other flags you need for math or system calls - see comments in timer.c). This is fairly
agressive optamization and it makes a difference in reducing your program overhead.
When you do this, be sure to verify that the copy actually happened; O3 optimization is smart
enough to tell that you are not using the results of the copy and optimize it out of
existence.

```
// Milisecond timer provided by Dr. Ernesto Gomez
#include time.h

/* compile with -lrt option to gcc */

double milisecond_timer(){
struct timespec itval;
/* returns system time in miliseconds */

	clock_gettime(CLOCK_REALTIME,&itval);
	return itval.tv_sec*1000+itval.tv_nsec/1e6;
}
```
