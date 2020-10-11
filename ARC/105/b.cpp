#include <bits/stdc++.h>
using namespace std;

int main(){
  // input
  int N;
  cin >> N;
  vector<int> a(N);
  int i;
  for (i = 0; i < N; ++i){
    cin >> a.at(i);
  }

  // compute
  sort(a.begin(), a.end());
  reverse(a.begin(), a.end());
  int X = a.at(0);
  int x = a.at(N-1);
  while (X != x){
    for (i = 0; i < N; ++i){
      if (a.at(i) == X){
        a.at(i) = X - x;
      }
      else{
        break;
      }
    }
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());
    X = a.at(0);
    x = a.at(N-1);
  }
  //output
  cout << a.at(0) << endl;
  return 0;
}
