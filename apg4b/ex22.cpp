#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

bool compare_by_second(pii ab1, pii ab2);

int main() {
  // input
  int N;
  cin >> N;
  vector<pii> ABs;
  int a, b;
  for (int i = 0; i < N; i++) {
    cin >> a >> b;
    ABs.push_back(make_pair(a, b));
  }

  // compute
  sort(ABs.begin(), ABs.end(), compare_by_second);

  // output
  for (auto AB: ABs) {
    tie(a, b) = AB;
    cout << a << " " << b << endl;
  }
}

bool compare_by_second(pii ab1, pii ab2) {
  return ab1.second < ab2.second;
}
