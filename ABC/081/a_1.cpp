#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int s;
  cin >> s;

  // compute
  int s1 = s / 100;
  int s2 = (s - s1*100) / 10;
  int s3 = s % 10;

  // output
  cout << s1 + s2 + s3 << endl;
}
