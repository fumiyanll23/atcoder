#include <stdio.h>
#include <string.h>

int main() {
  // input
  int K; scanf("%d", &K);
  int A, B; scanf("%d%d", &A, &B);

  // output
  if (A%K==0 || B%K==0 || (B-A+1)>=K) {
    printf("OK\n");
  }
  else {
    printf("NG\n");
  }
  return 0;
}
