#include <stdio.h>
#include <string.h>
#include <math.h>

typedef long long int lli;

int main() {
  // input
  lli N; scanf("%ld", &N);
  lli D; scanf("%ld", &D);
  lli a[N][2], i;
  for (i = 0; i < N; ++i) {
    scanf("%ld%ld", &a[i][0], &a[i][1]);
  }

  // compute
  int cnt = 0;
  for (i = 0; i < N; ++i) {
    if (a[i][0]*a[i][0]+a[i][1]*a[i][1] <= D*D) {
      cnt++;
    }
  }

  // output
  printf("%ld", cnt);
  return 0;
}
