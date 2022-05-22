#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  // ここにプログラムを追記
  int i = 0, j, score;
  string people;

  while (i < 2) {
  	if (i == 0) {
      people = "A";
      score = A;
    }
  	else {
      people = "B";
      score = B;
    }
    cout << people << ":";
    j = 0;
    while (j < score) {
      cout << "]";
      j++;
    }
    cout << endl;
    i++;
  }
}
