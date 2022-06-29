#include <stdio.h>
#include <string.h>

int main() {
  // input
  int S, W; scanf("%d%d", &S, &W);

  // output
  S<=W ? printf("unsafe\n"): printf("safe\n");
}
