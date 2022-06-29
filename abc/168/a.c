#include <stdio.h>
#include <string.h>

typedef long long int lli;

int main() {
  // input
  lli N; scanf("%lld", &N);

  // compute
  int dig = N % 10;

  // output
  if (dig == 3) {
    printf("bon\n");
  }
  else if (dig==0 || dig==1 || dig==6 || dig==8) {
    printf("pon\n");
  }
  else {
    printf("hon\n");
  }

  return 0;
}
