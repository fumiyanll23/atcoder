#include <bits/stdc++.h>
using namespace std;
 
int main(){
  int N;
  string S;
  cin >> N >> S;

  int ans = 0;
  int i, j;
  for(i = 0; i < N; ++i){
      int at = 0, cg = 0;
      for (j = i; j < N; ++j){
          if(S[j] == 'A'){
              at++;
          }
          else if(S[j] == 'T'){
              at--;
          }
          else if(S[j] == 'C'){
              cg++;
          }
          else{
              cg--;
          }
          if(at==0 && cg==0){
            ans++;
          }
      }
  }
  cout << ans << endl;

  return 0;
}