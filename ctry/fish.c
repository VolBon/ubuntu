#include <stdio.h>

typedef struct test {
	const char *food;
	int hours;
	} test_type;

typedef struct fish {
const char *name;
const char *species;
int teeth;
int age;
test_type test1;
} fish_type;

void catalog(fish_type f)
{
printf("%s is a %s with %i teeth. He is %i ///// hours %i\n",
f.name , f.species , f.teeth , f.age , f.test1.hours );
}

void label(fish_type f)
{
printf("%s %s %i %i\n",
f.name , f.species , f.teeth , f.age );
}

int main()
{

fish_type snappy = {"Snappy", "Piranha", 69, 4, {"me", 7}};
catalog(snappy);
label(snappy);
return 0;
}