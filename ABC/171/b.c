#include <stdio.h>
#include <string.h>

void mysort (int *x, int N);

int main() {
  // input
  int N, K; scanf("%d%d", &N, &K);
  int p[N], i;
  for (i = 0; i < N; ++i) {
    scanf("%d", &p[i]);
  }

  // compute
  int ans = 0;
  mysort(&p[0], N);
  for (i = 0; i < K; ++i) {
    ans += p[i];
  }

  // output
  printf("%d\n", ans);
  return 0;
}

/* Sort an array */
void mysort (int *x, int N) {
  int i, j;
  int tmp = 0;

  // compute
  for (i = 0; i < N; ++i) {
    for (j = 0; j < N; ++j) {
      if (x[i] < x[j]) {
        tmp = x[i];
        x[i] = x[j];
        x[j] = tmp;
      }
    }
  }
}
