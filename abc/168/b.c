#include <stdio.h>
#include <string.h>

int main() {
  // input
  int K; scanf("%d", &K);
  char S[101]; scanf("%s", &S[0]);

  // compute
  int N = strlen(S);

  // output
  if (N <= K) {
    printf("%s\n", S);
  }
  else {
    int i;
    char ans[102];
    for (i = 0; i < K+3; ++i) {
      if (i < K) {
        ans[i] = S[i];
      }
      else {
        ans[i] = '.';
      }
    }
    ans[K+3] = '\0';
    printf("%s\n", ans);
  }

  return 0;
}
