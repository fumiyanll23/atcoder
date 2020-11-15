#include <stdio.h>
#include <string.h>

int main(void) {
  // input
  int N, M; scanf("%d%d", &N, &M);

  // output
  printf("%d\n", (N*(N-1)+M*(M-1)) / 2);
  return 0;
}
