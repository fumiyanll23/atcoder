/* Sample 2 can not be working correctly... */
#include <stdio.h>
#include <string.h>
#include <math.h>

typedef long long int lli;

void mysort (lli *x, lli N);

int main() {
  // input
  lli N; scanf("%lld", &N);
  lli A[N], i;
  for (i = 0; i < N; ++i) {
    scanf("%lld", &A[i]);
  }

  // compute
  lli ans;
  mysort(&A[0], N);
  if (A[0] == 0) {
    ans = 0;
  }
  else {
    ans = 1;
    for (i = N-1; i > -1; --i) {
      ans *= A[i];
      if (ans >= pow(10, 18)){
        ans = -1;
        break;
      }
    }
  }

  // output
  printf("%lld\n", ans);
  return 0;
}

/* Sort an array */
void mysort (lli *x, lli N) {
  lli i, j;
  lli tmp = 0;

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
