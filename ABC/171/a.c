#include <stdio.h>
#include <string.h>

int main() {
  // input
  char alph; scanf("%c", &alph);

  // compute
  alph = (int)alph;

  // output
  if (alph <= 90) {
    printf("A\n");
  }
  else
  {
    printf("a\n");
  }
  return 0;
}
