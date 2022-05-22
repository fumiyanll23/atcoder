#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  // Write below...
  vector<int> scores(N);
  int sum = 0;
  // 入力を受け取ると同時に、合計点を求める
  for (int i = 0; i < N; i++) {
    cin >> scores.at(i);
    sum += scores.at(i);
  }
  // 平均点を求める
  int mean = sum / N;
  for (int i = 0; i < N; i++) {
    cout << abs(mean - scores.at(i)) << endl;
  }
}
