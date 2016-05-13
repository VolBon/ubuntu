#include <stdio.h>
#include <limits.h>
#include <float.h>

int main()
{
	printf("%i\n", CHAR_MAX);
	printf("The value of INT_MIN is %i\n", CHAR_MIN);
	printf("The value of FLT_MAX is %f\n", FLT_MAX);
	printf("The value of FLT_MIN is %.50f\n", FLT_MIN);
	printf("The value of FLT_MAX is %f\n", DBL_MAX);
	printf("The value of FLT_MIN is %.50f\n", DBL_MIN);
		
	
	return 0;
}