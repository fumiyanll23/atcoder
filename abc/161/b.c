#include <stdio.h>
#include <string.h>

int main(void) {
  // input
  int N, M; scanf("%d%d", &N, &M);
  int A[N], i;
  for (i = 0; i < N; ++i) {
    scanf("%d", &A[i]);
  }

  // compute
  int sum = 0;
  for (i = 0; i < N; ++i) {
    sum += A[i];
  }
  int cnt = 0;
  double accept = sum / (4*M);
  for (i = 0; i < N; ++i) {
    if (A[i] >= accept) {
      cnt++;
    }
  }

  // output
  if (accept >= M) {
    printf("Yes\n");
  }
  else {
    printf("No\n");
  }
  return 0;
}
