#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int N;
  cin >> N;
  set<int> ds;
  for (int i = 0; i < N; i++) {
    int d;
    cin >> d;
    ds.insert(d);
  }

  // compute

  // output
  cout << ds.size() << endl;
}
