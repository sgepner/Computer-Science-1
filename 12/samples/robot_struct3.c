#include <stdio.h>
#include <string.h>

typedef struct Robot{
  char name[50];
  double x, y;
  
  void(*print)(struct Robot* pr);
  
} robot;

void PrintRobot(robot* pr)
{
  printf("This is a robot!\n");
  printf("Robot name is: %s\n", pr->name);
  printf("Position: (%lf, %lf)\n", pr->x, pr->y);
}

int main(){
  robot r1, r2, r3, r2d2;
  
  r1.print = PrintRobot;
  r2.print = PrintRobot;
  r3.print = PrintRobot;
  r3.print = PrintRobot;
  
  strcpy(r1.name, "This is a Robot!");
  r1.x=0; r1.y=100;
  
  r1.print(&r1);
  
}
