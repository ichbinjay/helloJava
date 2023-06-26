#include<iostream>

using namespace std;
int main(){
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        int s1 = 0, s2 = 0;
        for(int i = 0; i < n; i++){
            int x; cin >> x;
            s1 += x;
        }
        for(int i = 0; i < m; i++){
            int x; cin >> x;
            s2 += x;
        }
        if(s1 > s2) cout << "Tsondu\n";
        else if (s1 < s2) cout << "Tenzing\n";
        else cout << "Draw\n";
    }
}