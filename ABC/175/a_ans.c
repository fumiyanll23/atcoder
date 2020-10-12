#include <stdio.h>
#include <string.h>

int main(){
  // input
  char S[3]; scanf("%s", S);

  // compute
  char R = 'R';
  int p = !strcmp(S[0], R);
  int q = !strcmp(S[1], R);
  int r = !strcmp(S[2], R);
   // output
  if (p && q && r){
    printf("3\n");
  }
  else if ((p&&q) || (q&&r)){
    printf("2\n");
  }
  else if (p || q || r){
    printf("1\n");
  }
  else{
    printf("0\n");
  }
  return 0;
}

// Received "Error code: 139"...
