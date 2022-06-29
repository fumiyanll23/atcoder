#include <stdio.h>
#include <string.h>

int main() {
  // input
  int N, K; scanf("%d%d", &N, &K);
  int sunuke[101], i;
  for (i = 0; i < 101; ++i) {
    sunuke[i] = 0;
  }
  int d[K], j;
  for (i = 0; i < K; ++i) {
    scanf("%d", &d[0]);
    for (j = 0; j < d[i]; ++j) {
      int A[d[i]];
      scanf("%d", &A[j]);
      sunuke[A[j]]++;
    }
  }

  // compute
  int ans = 0;
  for (i = 0; i < N; ++i) {
    if (sunuke[i] == 0) {
      ans++;
    }
  }

  // output
  printf("%d\n", ans);
  return 0;
}
