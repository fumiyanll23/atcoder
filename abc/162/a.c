#include <stdio.h>
#include <string.h>

int main() {
  // input
  char N[4]; scanf("%s", &N[0]);

  // compute
  int i, flag = 0;
  for (i = 0; i < 3; ++i) {
    if (!strcmp(&N[i], "7")) {
      flag = 1;
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
