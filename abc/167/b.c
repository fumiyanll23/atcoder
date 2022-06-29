#include <stdio.h>
#include <string.h>

typedef long long int lli;

int main() {
  // input
  lli A, B, C, K;
  scanf("%lld%lld%lld%lld", &A, &B, &C, &K);

  // compute
  lli ans;
  if (K <= A) { // 1<=K<=A
    ans = K;
  }
  else if (K <= A+B) { // A<K<=A+B
    ans = A;
  }
  else { // A+B<K
    ans = A - (K-(A+B));
  }

  // output
  printf("%lld\n", ans);
  return 0;
}
