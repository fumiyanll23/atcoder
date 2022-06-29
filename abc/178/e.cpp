#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> x(N);
  vector<int> y(N);
  int i;
  for(i = 0; i < N; i++){
    cin >> x.at(i) >> y.at(i);
  }

  vector<vector<int>> d(N, vector<int>(N));
  int j;
  for(i = 0; i < N; i++){
    for(j = 0; j < N; j++){
      if(i < j){
        d.at(i).at(j) = abs(x.at(i)-x.at(j)) + abs(y.at(i)-y.at(j))
      }
    }
  }

  max(max(d)) // Is it correct??
}