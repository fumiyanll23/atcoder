#include <stdio.h>
#include <string.h>

int main(){
  char S[10000]; scanf("%s", S);

  int N = strlen(S);
  if(S[N-1] != 's'){
    S[N] = 's';
    S[N+1] = NULL;
  }
  else{
    S[N] = 'e';
    S[N+1] = 's';
    S[N+2] = NULL;
  }

  printf("s\n", S);
  return 0;
}