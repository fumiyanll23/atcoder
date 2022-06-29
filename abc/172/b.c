#include <stdio.h>
#include <string.h>

typedef long long int lli;

int main() {
  // input
  char S[200001]; scanf("%s", &S);
  char T[200001]; scanf("%s", &T);

  // compute
  lli s = strlen(S);
  lli diff = 0;
  int i;
  for (i = 0; i < s; ++i) {
    if (S[i] != T[i]) {
      diff++;
    }
  }
  // output
  printf("%ld\n", diff);
  return 0;
}
