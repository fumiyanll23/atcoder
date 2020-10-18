#include <stdio.h>
#include <string.h>

typedef long long int lli;

int main() {
  // input
  lli N; scanf("%ld", &N);
  int i;
  int ac = 0, wa = 0, tle = 0, re = 0;
  char S[3];

  // compute
  for (i = 0; i < N; ++i) {
    scanf("%s", &S[0]);
    if (!(strcmp(S, "AC"))) {
      ac++;
    }
    else if (!(strcmp(S, "WA"))) {
      wa++;
    }
    else if (!(strcmp(S, "TLE"))) {
      tle++;
    }
    else {
      re++;
    }
  }

  // output
  printf("AC x %d\n", ac);
  printf("WA x %d\n", wa);
  printf("TLE x %d\n", tle);
  printf("RE x %d\n", re);
  return 0;
}
