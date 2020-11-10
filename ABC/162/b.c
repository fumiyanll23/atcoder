#include <stdio.h>
#include <string.h>

typedef long long int lli;

int main(void) {
  // input
  int N; scanf("%d", &N);

  // compute
  lli ans = 0;
  int i;
  for (i = 0; i < N+1; ++i) {
    if (i%3!=0 && i%5!=0) {
      ans += i;
    }
  }

  // output
  printf("%lld\n", ans);
  return 0;
}
