#include <bits/stdc++.h>
using namespace std;

int main() {
  int H, W, i;
  cin >> H >> W;
  vector<string> pic(H);

  for(i = 0; i < H; i++){
    cin >> pic.at(i);
  }

  // 以降, 出力する
  for(i = 0; i < W+2; i++){
    cout << '#';
  }
  cout << endl;
  for(i = 0; i < H; i++){
    cout << '#' << pic.at(i) << '#' << endl;
  }
  for(i = 0; i < W+2; i++){
    cout << '#';
  }
  cout << endl;
}
