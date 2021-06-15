#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> a(N);
  int i;
  for(i = 0; i < N; i++){
    cin >> a.at(i);
  }
  sort(a.begin(), a.end());
  reverse(a.begin(), a.end());
  int A = 0;
  int B = 0;
  for(i = 0; i < N; i++){
    if(i%2 == 0){
      A += a.at(i);
    } else{
      B += a.at(i);
    }
  }
  cout << A - B << endl;
}
