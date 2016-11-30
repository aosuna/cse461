#ifdef __cplusplus ////used to include a c file into c++
extern "C" {
#endif
#include <time.h>
#include <stdio.h>

/* compile with -lrt option to gcc */

double milisecond_timer(){
struct timespec itval;
/* returns system time in miliseconds */

	clock_gettime(CLOCK_REALTIME,&itval);
	return (itval.tv_sec*1000+itval.tv_nsec)/1e6;
}

#ifdef __cplusplus //used to include a c file into c++
	}
#endif