#include <stdio.h>

void change(int *x, int *y){
	//x = x+1;
	
	*x = *x + 99;
	*y = *y - 99;
	
	printf("%p, %p", x, y);
  
}

int main(){
  int ex = 4;
  int ey = 4;
  
  char name[5];
  

  change(&ex, &ey);
  
  fgets(name, 5, stdin);
  printf("%s", name);

  printf("New values %i, %i \n", ex, ey);
}