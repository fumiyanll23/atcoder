#include <stdio.h>
#include <string.h>

int main() {
  // input
  char S[11]; scanf("%s", &S[0]);
  int N = strlen(S);
  char T[N+1]; scanf("%s", &T[0]);

  // compute
  char test[N+1];
  int i;
  for (i = 0; i < N; ++i) {
    test[i] = T[i];
  }
  test[N] = '\0';

  // output
  if (!strcmp(&S[0], &test[0])) {
    printf("Yes\n");
  }
  else {
    printf("No\n");
  }
  return 0;
}
