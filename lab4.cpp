#include "timer.c"
#include <vector>
#include <iostream>
#include <sys/time.h>

//how to compile --> g++ -O3 -o time lab4.cpp

//run sysctl -a | grep cache to see cache size avaiable on MAC OS. 
using namespace std;

int main(){
	//create 2 arrays
	//size of array needs to be bigger than CACHE
	long size = 2000000000; // set array size to 5K
	double A[size];
	double B[size];

	//init A
	srand (time(NULL));
	for(int i = 0; i < size; i++){
		A[i] = rand()%size;
	}
	
	double X = milisecond_timer();
	double Y = 0;

	//copy A -> B
	for (int i = 0; i < size; i++){
		B[i] = A[i];
		Y += milisecond_timer() - X;
	}
	
	double time = Y - X;
	double bandwidth = size / time;

	printf("\nX value = %f\n", X);
	printf("Y value = %f\n", Y);

	printf("Time to execute is %f\n", time);
	printf("bandwidth: %f\n", bandwidth);

	return 0;
}