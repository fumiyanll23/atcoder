#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int N;
  cin >> N;
  int  num = N, dig = 0, sum = 0;

  // compute
  while (num != 0) {
    dig = num % 10;
    sum += dig;
    num = (num - dig) / 10;
  }

  // output
  if (N%sum == 0) {
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }
}
