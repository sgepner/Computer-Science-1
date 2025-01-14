#include <stdio.h>
#include <math.h>

int main(){
  int a;
  scanf("%d", &a);
  
  double b = pow(a, 2);//a^2 => a*a
  double c = pow(a, 2.31);//a^2 => ???
  printf(" %d %lf %lf\n", a, b, c);
}
