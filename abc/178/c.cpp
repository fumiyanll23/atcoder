#include <bits/stdc++.h>
using namespace std;

int factorial(int n);

int main(){
  int N;
  cin >> N;
  int i, p = 1;
  for(i = 0; i < 9; i++){
    p *= 10;
  }

  if(N == 1){
    cout << 0 << endl;
  }
  else if(N == 2){
    cout << 1 << endl;
  }
  else{
    int comb = factorial(N) / factorial(N-2);
    int remain = 1;
    for(i = 0; i < N-2; i++){
      remain *= 10;
    }
    
    cout << (comb*remain) % p << endl;
  }
}

int factorial(int n){
    int sum = 1;
    for (int i = 1; i <= n; ++i)
    {
        sum *= i;
    }
    return sum;
}