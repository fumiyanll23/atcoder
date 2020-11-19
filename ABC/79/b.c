/* TLE ...... */

#include <stdio.h>
#include <string.h>

typedef long long int lli;

lli lucas_number(lli N);

int main(void) {
  // input
  lli N; scanf("%lld", &N);

  // output
  printf("%lld\n", lucas_number(N));
  return 0;
}


lli lucas_number(lli N) {
  if (N == 0) {
    return 2;
  }
  else if (N == 1) {
    return 1;
  }
  else if (N >= 2) {
    return lucas_number(N-1) + lucas_number(N-2);
  }
}
