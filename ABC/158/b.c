#include <stdio.h>
#include <string.h>

typedef long long int lli;

int main(void) {
  // input
  lli N, A, B; scanf("%lld%lld%lld", &N, &A, &B);

  // compute & output
  lli q = N / (A+B);
  lli r = N % (A+B);
  if (r == 0) {
    printf("%lld\n", A * q);
  }
  else if (r < A) {
    printf("%lld\n", A*q + r);
  }
  else {
    printf("%lld\n", A*q + A);
  }

  return 0;
}
