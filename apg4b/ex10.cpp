#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  // ここにプログラムを追記
  int i = 0, j = 0;

  // Aの棒グラフを表示する
  cout << "A:";
  while (i < A) {
    cout << "]";
    i++;
  }
  cout << endl;

  // Bの棒グラフを表示する
  cout << "B:";
  while (j < B) {
    cout << "]";
    j++;
  }
  cout << endl;
}
