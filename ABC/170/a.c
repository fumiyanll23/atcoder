#include <stdio.h>
#include <string.h>

int main() {
  // input
  int x[5], i;
  for (i = 0; i < 5; ++i) {
    scanf("%d", &x[i]);
  }

  // compute
  int ans;
  for (i = 0; i < 5; ++i) {
    if (x[i] == 0) {
      ans = i + 1;
    }
  }

  // output
  printf("%d\n", ans);
  return 0;
}
