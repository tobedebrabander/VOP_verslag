#include "../common.h"
#include "../randArr.h"

#define ITER 2048
#define STRIDE 2
#define ARRAY_SIZE 5

__attribute__((noinline))
int main(int argc, char* argv[])
{
	int data[5] = {1,2,3,4,5};
	int indices[ITER];
	int t = 0;
	int i = 0;
	int a = 0;
	
	ROI_BEGIN();
	for(i = 0; i < ITER; ++i)
	{
		indices[a] = (i * STRIDE) % ARRAY_SIZE;
		a += randArr[i];
	}

	for(i = 0; i < a; ++i)
	{
		t += data[indices[i]];
	}
	ROI_END();
}
