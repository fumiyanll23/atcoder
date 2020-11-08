#include <stdio.h>
#include <string.h>

int main() {
  // input
  int N, M; scanf("%d%d", &N, &M);
  int A[M], i;
  for (i = 0; i < M; ++i) {
    scanf("%d", &A[i]);
  }

  // compute
  int homework = 0;
  for (i = 0; i < M; ++i) {
    homework += A[i];
  }

  // output
  if (N >= homework) {
    printf("%d\n", N-homework);
  }
  else {
    printf("-1\n");
  }
  return 0;
}
