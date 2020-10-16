#include <stdio.h>
#include <string.h>

int main() {
  // input
  int N; scanf("%d", &N);

  // compute
  int money = N/1000 + 1;

  // output
  if (N%1000 == 0) {
    printf("0\n");
  }
  else {
    printf("%d\n", 1000*money - N);
  }
  return 0;
}
