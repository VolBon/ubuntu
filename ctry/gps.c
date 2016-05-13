#include <stdio.h>
int main()
{
	float latitude;
	float longitude;
	char info[80];
	int started = 0;
	puts("data=[");
	
	while (scanf("%f,%f,%79[^\n]", &latitude, &longitude, info) == 3) {
		if (started)
			printf(",\n");
	else
		started = 1;
		if(-90>latitude || latitude>90){
			fprintf(stderr, "Error 2");
			return 2;
			}

		if(-180>longitude || longitude>180){
			fprintf(stderr, "Error 2");
			return 2;
			}
		else
			printf("{latitude: %f, longitude: %f, info: '%s'}", latitude, longitude, info);
	}
	puts("\n]");
	return 0;
}