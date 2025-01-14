#include <stdio.h>
#include <math.h>

double derivative( double (fun)(double) , double x, double h)
{
  return (fun(x+h) - fun(x)) / h; 
}

double fun(double x)
{
  return x*x*x*x+4*x*x*x -8*x*x +5;
}

int main(){
  double d1 = derivative(sin, 0, 0.0001);
  printf("%lf\n", d1);
}
