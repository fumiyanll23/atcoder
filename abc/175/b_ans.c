#include <stdio.h>
#include <string.h>

void mysort (int *x, int N);

int main(){
  // input
  int N; scanf("%d", &N);
  int i, j, k, L[N];
  for (i = 0; i < N; ++i){
    scanf("%d", &L[i]);
  }

  // compute
  mysort(L, N);
  int cnt = 0;
  for (i = 0; i < N; ++i){
    for (j = 0; j < i; ++j){
      for (k = 0; k < j; ++k){
        if (L[i]!=L[j] && L[j]!=L[k] && L[k]+L[j] > L[i]){
          cnt++;
        }
      }
    }
  }

  // output
  printf("%d\n", cnt);
  return 0;
}

void mysort (int *x, int N) {
  int i, j;
  int tmp = 0;

  // compute
  for (i = 0; i < N; ++i) {
    for (j = i; j < N; ++j) {
      if (x[i] > x[j]) {
        tmp = x[i];
        x[i] = x[j];
        x[j] = tmp;
      }
    }
  }
}
