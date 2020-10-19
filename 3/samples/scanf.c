#include <stdio.h>

int main(){
  int a;
  double b;
  
  printf(" Give me an int!\n");
  scanf("%d", &a); //mind the &!!
  
  printf(" Give me an double!\n");
  scanf("%lf", &b);
  
  printf("a=%d b=%lf\n", a,b );
}
