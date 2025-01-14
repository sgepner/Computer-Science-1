#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int n1, n2;
  scanf("%d\n", &n1);
  char *p1=(char*)malloc(n1*sizeof(char));
  
  fgets( p1, n1, stdin );
  p1[ strlen(p1) - 1 ] = '\0';
//  printf("%s\n", p1);

  scanf("%d\n", &n2);
  char *p2=(char*)malloc(n2*sizeof(char));
  fgets( p2, n2, stdin );
  p2[ strlen(p2) - 1 ] = '\0';
//  printf("%s\n", p2);

  char *p3=(char*)malloc(( strlen(p1)+ strlen(p2))*sizeof(char));
  
  strcat(p3, p1);
  strcat(p3, p2);
  
//  printf("%s\n", p1);
//  printf("%s\n", p2);
  printf("%s\n", p3);
  
  free(p1);  
  free(p2);
  free(p3);
}
