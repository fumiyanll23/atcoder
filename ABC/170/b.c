#include <stdio.h>
#include <string.h>

int main() {
  // input
  int X, Y; scanf("%d%d", &X, &Y);

  // compute
  int i, j, flag = 0;
  for (i = 0; i < 100; ++i) {
    for (j = 0; j < 100; ++j) {
      if (i+j==X && 2*i+4*j==Y) {
        flag = 1;
      }
    }
  }

  // output
  if (flag) {
    printf("Yes\n");
  }
  else {
    printf("No\n");
  }
  return 0;
}
