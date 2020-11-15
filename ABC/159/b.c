// Now Underconstructing ...

#include <stdio.h>
#include <string.h>

int palindromeChecker(char* S, int N);

int main(void) {
  // input
  char S[100]; scanf("%s", &S[0]);

  // compute
  int N = strlen(S);
  int a = palindromeChecker(&S[0], N);

  // output
  if (a && b && c) {
    printf("Yes\n");
  }
  else {
    printf("No\n");
  }
  return 0;
}


// define function palindromeChecker()
int palindromeChecker(char* S, int N) { // N is required to be odd.
  int half = N/2, flag = 1, i;

  // compute
  for (i = 0; i < half; ++i) {
    if (S[i] != S[N-1-i]) {
      flag = 0;
    }
  }

  // output
  return flag;
}
