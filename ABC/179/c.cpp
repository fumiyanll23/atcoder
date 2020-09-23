#include <bits/stdc++.h>

using namespace std;

int main(){
 int N;
 cin >> N;

 long long i, j, cnt = 0;
 for(i=1; i<N; i++){
   for(j=1; j<N; j++){
     if(i*j < N){
       cnt++;
     }
   }
 }
 
 cout << cnt << endl;
}