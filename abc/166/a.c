#include <stdio.h>
#include <string.h>

int main() {
  // input
  char S[4]; scanf("%s", &S[0]);

  // output
  char abc[4] = "ABC", arc[4] = "ARC";
  if (!strcmp(&S[0], &abc[0])) {
    printf("%s\n", arc);
  }
  else
  {
    printf("%s\n", abc);
  }
  return 0;

}
