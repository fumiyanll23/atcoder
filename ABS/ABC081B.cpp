#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  int i;
  vector<int> num(N);
  vector<int> count(N);
  for(i = 0; i < N; i++){
    cin >> num.at(i);
  }
  for(i = 0; i < N; i++){
    while(num.at(i)%2 == 0){
      num.at(i) /= 2;
      count.at(i)++;
    }
  }
  sort(count.begin(), count.end());
  cout << count.at(0) << endl;
}
