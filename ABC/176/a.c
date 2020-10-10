#include <stdio.h>
#include <string.h>

int main(){
  // input
  int N, X, T; scanf("%d%d%d", &N, &X, &T);

  // compute
  int time = N / X;

  // output
  if (N%X == 0){
    printf("%d", time * T);
  }
  else{
    printf("%d", (time+1) * T);
  }
  return 0;
}