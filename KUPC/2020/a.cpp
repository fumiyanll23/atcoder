#include <bits/stdc++.h>
using namespace std;

int main(){
  // input
  int N;
  cin >> N;
  vector<vector<int>> dis(N, vector<int>(2));
  int i;
  for (i = 0; i < N; ++i){
    cin >> dis.at(i).at(0) >> dis.at(i).at(1);
  }

  // calculate
  int ans = 0;
  for (i = 0; i < N-1; ++i){
    ans += abs(dis.(i+1).at(0)-dis.at(i).at(0)) + abs(dis.at(i+1).at(1)-dis.at(i).at(1));
  }

  // output
  cout << ans << endl;
}

// Why did I receive compile errors?