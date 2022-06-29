#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int N;
  string S, ans = "Three";
  bool P = false, W = false, G = false, Y = false;
  cin >> N;

  // compute
  for (int i = 0; i < N; i++) {
    cin >> S;
    if (S == "P") {
      P = true;
    }
    else if (S == "W") {
      W = true;
    }
    else if (S == "G") {
      G = true;
    }
    else {
      Y = true;
    }
  }
  if (P && W && G && Y) {
    ans = "Four";
  }

  // output
  cout << ans << endl;
}
