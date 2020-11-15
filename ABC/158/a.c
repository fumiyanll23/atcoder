#include <stdio.h>
#include <string.h>

int main(void) {
  // input
  char S[4]; scanf("%s", &S[0]);

  // compute
  char aaa[4] = "AAA";
  char bbb[4] = "BBB";

  // output
  if (!strcmp(&S[0], &aaa[0]) || !strcmp(&S[0], &bbb[0])) {
    printf("No\n");
  }
  else {
    printf("Yes\n");
  }
  return 0;
}
