#include <bits/stdc++.h>
using namespace std;

int main() {
  int K;
  cin >> K;
  int i, j, k;
  int ans = 0;
  
  for(i = 1; i < K; i++){
    for(j = 1; j < K; j++){
      for(k = 1; k < K; k++){
        ans += gcd(gcd(i, j), k);
      }
    }
  }
  cout << ans << endl;
}

// Sample1 outputs 1 and sample2 outputs 10611772