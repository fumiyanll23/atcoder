#include <stdio.h>
#include <string.h>

int main(void) {
  // input
  int N; scanf("%d", &N);

  // compute
  int a = N / 100;
  int b = N % 100 / 10;
  int c = N % 10;

  // output
  if (a==7 || b==7 || c==7) {
    printf("Yes\n");
  }
  else {
    printf("No\n");
  }
  return 0;
}
