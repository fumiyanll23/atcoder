#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int main() {
  // input
  int N;
  cin >> N;
  vector<pii> ABs;
  int a, b;
  for (int i = 0; i < N; i++) {
    cin >> b >> a;
    ABs.push_back(make_pair(a, b));
  }

  // compute
  sort(ABs.begin(), ABs.end());

  // output
  for (auto AB: ABs) {
    tie(b, a) = AB;
    cout << a << " " << b << endl;
  }
}
