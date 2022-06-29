#include <bits/stdc++.h>
using namespace std;

int main(){
  int i, count = 0;
  string str;
  cin >> str;

  for(i = 0; i < 3; i++){
    if(str.at(i) == '1'){
      count++;
    }
  }
  cout << count << endl;
}
