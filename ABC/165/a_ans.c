#include <stdio.h>
#include <string.h>

int main() {
  // input
  int K; scanf("%d", &K);
  int A, B; scanf("%d%d", &A, &B);

  // compute
  int max = (B / K) * K;

  // output
  if (A <= max) {
    printf("OK\n");
  }
  else {
    printf("NG\n");
  }
  return 0;
}
