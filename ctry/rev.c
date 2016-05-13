#include <stdio.h>
#include <string.h>

void reverse(char *s){
	size_t len = strlen(s);
	char *t = s + len -1;
	
	while(t>=s){
		printf("%c", *t);
		t = t - 1;
		}
	puts("");
	}
	
int main(){
	char *name[] = {"name", "surname", "something"};
	char a[20] = "new";
	
	strcpy(a, name[0]);
	strcat(a, name[1]);
	
	printf("%s\n", a);
	
	printf("%p\n", &name[0]);
	reverse(name[0]);
	reverse(name[1]);
	reverse(name[2]);
	return 0;
}