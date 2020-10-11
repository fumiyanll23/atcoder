#include <stdio.h>
#include <string.h>

int main(){
  // input
  char *N; scanf("%s", N);

  // compute
  int i, sum = 0;
  for (i = 0; i < strlen(N); ++i){
    sum += N[i];
  }

  // output
  if (sum%9 == 0){
    printf("Yes");
  }
  else{
    printf("No");
  }
  return 0;
}

// Run but not correct...
