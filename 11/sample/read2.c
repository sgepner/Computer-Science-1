#include <stdio.h>

int main(){
  char a[10];
  
  //char *p = fgets( a, 256, stdin );
  fgets( a, 10, stdin );
  
  printf("%s\n", a);
  //printf("%c %p\n", *p, p);
  printf("%c %p\n", a[0], a);
}
