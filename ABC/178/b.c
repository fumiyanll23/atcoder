#include <stdio.h>
#include <string.h>
typedef long long int lli;

lli mymax(lli len, lli *num);

int main(){
  // input
  lli a, b, c, d; scanf("%d%d%d%d", &a, &b, &c, &d);

  //calculate
  lli num[] = {a*c, a*d, b*c, b*d};

  // output
  printf("%d\n", mymax(4, num));

  return 0;
}

// find max
lli mymax(lli len, lli *num){
  lli i, max = num[0];

  for (i = 1; i < len; ++i){
    if (num[i] > max){
      max = num[i];
    }
  }

  return max;
}