#include <stdio.h>
#include <string.h>

int mymin(int a, int b);

int main(){
  // input
  char S[1000]; scanf("%s", S);
  int s = strlen(S);
  char T[s]; scanf("%s", T);
  int t = strlen(T);

  //calculate
  int ans = t;
  int i, j;
  for (i = 0; i < s-t+1; ++i){
    int diff = 0;
    for (j = 0; j < t; ++j){
      if (T[j] != S[i+j]){
        diff++;
      }
    }
    ans = mymin(ans, diff);
  }

  // output
  printf("%d", ans);
  return 0;
}

// find min
int mymin(int a, int b){
  if (a >= b){
    return b;
  }
  else{
    return a;
  }
}