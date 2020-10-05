#include <stdio.h>
#include <string.h>

int main(){
  // input
  int N; scanf("%d", &N);
  int i, j, D[N][2];
  for(i = 0; i < N; ++i){
    for(j = 0; j < 2; ++j){
      scanf("%d", &D[i][j]);
    }
  }
  
  // judge
  int flag = 0;
  for(i = 0; i < N-2; ++i){
    if(D[i][0]==D[i][1] && D[i+1][0]==D[i+1][1] && D[i+2][0]==D[i+2][1]){
      flag = 1;
    }
  }

  // output
  if(flag){
    printf("Yes\n");
  }
  else{
    printf("No\n");
  }

  return 0;
}