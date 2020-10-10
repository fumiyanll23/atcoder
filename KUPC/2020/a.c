#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
  // input
  int N; scanf("%d", &N);
  int i, dis[N][2];
  for (i = 0; i < N; ++i){
    scanf("%d%d", &dis[i][0], &dis[i][1]);
  }

  // calculate
  int ans = 0;
  for (i = 0; i < N-1; ++i){
    ans += abs(dis[i+1][0]-dis[i][0]) + abs(dis[i+1][1]-dis[i][1]);
  }

  // output
  printf("%d", ans);
  return 0;
}

// Why did I receive "WA"?