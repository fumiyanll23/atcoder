#include <stdio.h>
#include <string.h>

int main() {
  // input
  int A, B, C, D; scanf("%d%d%d%d", &A, &B, &C, &D);

  // compute
  int winner; // 0 -> Aoki-kun; 1 -> Takahashi-kun
  if (A%D == 0) {
    if (C%B == 0) {
      if (A/D >= C/B) {
        winner = 1;
      }
      else {
        winner = 0;
      }
    }
    else {
      if (A/D >= C/B+1) {
        winner = 1;
      }
      else {
        winner = 0;
      }
    }
  }
  else {
    if (C%B == 0) {
      if (A/D+1 >= C/B) {
        winner = 1;
      }
      else {
        winner = 0;
      }
    }
    else {
      if (A/D+1 >= C/B+1) {
        winner = 1;
      }
      else {
        winner = 0;
      }
    }
  }

  // output
  if (winner) {
    printf("Yes\n");
  }
  else {
    printf("No\n");
  }
  return 0;
}
