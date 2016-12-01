#include <iostream>
#include "timer.c"
//how to compile --> g++ -O3 -o time lab4.cpp
//run sysctl -a | grep cache to see cache size avaiable on MAC OS. 
using namespace std;

int main(){
	long size = 5e8; //size of array needs to be bigger than CACHE
	double A[size];  //create 2 arrays
	double B[size];
	double Y = 0;

	//init A
	srand(time(NULL));
	for(int i = 0; i < size; i++){
		A[i] = rand()%(10000);
	}
	double X = milisecond_timer();
	//copy A -> B
	for (int i = 0; i < size; i++){
		B[i] = A[i];
		if(i == size-1)
			Y = milisecond_timer();
	}
	double time = (Y - X);
	double bandwidth = (size) / (time/1000);
	
	printf("\nX value = %f ms\n", X);
	printf("Y value = %f ms\n", Y);

	printf("Time to execute is %f ms\n", time);
	printf("bandwidth: %f bytes/s\n", bandwidth);

	return 0;
}