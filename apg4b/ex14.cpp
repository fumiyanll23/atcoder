#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  // Write below...
  int tallest = max(max(A, B), C);
  int shortest = min(min(A, B), C);
  cout << tallest - shortest << endl;
}
