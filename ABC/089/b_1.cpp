#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int N;
  string S, ans = "Three";
  cin >> N;

  // compute
  for (int i = 0; i < N; i++) {
    cin >> S;
    if (S == "Y") {
      ans = "Four";
    }
  }

  // output
  cout << ans << endl;
}
