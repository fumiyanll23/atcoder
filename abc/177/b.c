#include <stdio.h>
#include <string.h>
// typedef long long int lli;

int mymin(int len, int *num);

int main(){
  // input
  char S[1000]; scanf("%s", S);
  int s = strlen(S);
  char T[s]; scanf("%s", T);
  int t = strlen(T);

  //  calculate
  int i = 0, j = 0;
  int diff[s-t+1];
  char target[t];
  strncpy(target, i, t);
  target[t] = "\0";
  for (i = 0; i < s-t+1; ++i){
    diff[i] = 0;
  }
  for (i = 0; i < s-t+1; ++i){
    // char target[t];
    strncpy(target, i, t);
    // target[t] = "\0";
    for (j = 0; j < t; ++j){
      if (target[j] != T[j]){
        diff[i]++;
      }
    }
  }

  // output
  printf("%d", mymin(s-t+1, diff));
  return 0;
}

// find min
int mymin(int len, int *num){
  int i, min = num[0];

  for (i = 1; i < len; ++i){
    if (num[i] < min){
      min = num[i];
    }
  }

  return min;
}

// Buffer over flow...