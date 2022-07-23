#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int N;
  cin >> N;
  int A;
  map<int, int> am;
  for (int i = 0; i < N; i++) {
    cin >> A;
    if (am.count(A)) {
      am.at(A)++;
    }
    else {
      am[A] = 1;
    }
  }

  // compute
  int ans_key = 0;
  int ans_val = 0;
  for (auto p: am) {
    int k = p.first;
    int v = p.second;
    if (v > ans_val) {
      ans_key = k;
      ans_val = v;
    }
  }

  // output
  cout << ans_key << " " << ans_val << endl;
}
