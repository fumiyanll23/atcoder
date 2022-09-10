#include <bits/stdc++.h>
using namespace std;

int dig_sum(int n);

int main() {
  // input
  int N, A, B;
  cin >> N >> A >> B;

  // compute
  int ans = 0;
  for (int i = 1; i < N + 1; i++) {
    int sum = dig_sum(i);
    if (A <= sum && sum <= B) {
      ans += i;
    }
  }

  // output
  cout << ans << endl;
}

int dig_sum(int n) {
  int sum = 0;
  while (n > 0) {
    sum += n % 10;
    n /= 10;
  }

  return sum;
}
