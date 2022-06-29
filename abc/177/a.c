#include <stdio.h>
#include <string.h>

int main(){
  // input
  double D, T, S; scanf("%lf%lf%lf", &D, &T, &S);

  // output
  printf("%s\n", (D/S <= T)? "Yes": "No") ;

  return 0;
}