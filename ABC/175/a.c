#include <stdio.h>
#include <string.h>

int main(){
  // input
  char S[3]; scanf("%s", S);

  // compute
  char *RRR = "RRR";
  char *SRR = "SRR";
  char *RRS = "RRS";
  char *SSS = "SSS";

  // output
  if (!strcmp(S, RRR)){
    printf("3\n");
  }
  else if (!strcmp(S, SRR) || !strcmp(S, RRS)){
    printf("2\n");
  }
  else if (!strcmp(S, SSS)){
    printf("0\n");
  }
  else{
    printf("1\n");
  }
  return 0;
}
