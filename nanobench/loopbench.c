#include "common.h"

#define ITER 3

__attribute__ ((noinline))
int main(int argc, char* argv[]) {
	int a = 0;
	
	ROI_BEGIN();
	for(int i = 0; i < ITER; i+=1) {
		a++;
	}
	ROI_END();
}
