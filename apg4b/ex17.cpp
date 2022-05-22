#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, S;
  cin >> N >> S;
  vector<int> A(N), P(N);
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }
  for (int i = 0; i < N; i++) {
    cin >> P.at(i);
  }

  // リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
  // ここにプログラムを追記
  int ans = 0;

  for (int ai = 0; ai < N; ai++) {
    for (int pj = 0; pj < N; pj++) {
      if (A.at(ai) + P.at(pj) == S) {
        ans += 1;
      }
    }
  }

  cout << ans << endl;
}
