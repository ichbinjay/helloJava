#include<iostream>
using namespace std;

int main(){
    int t; cin >> t;
    while(t--){
        int x, y; cin >> x >> y;
        if(x <= 8){
            if(x*y < 500) cout << "Yes" << endl;
            else cout << "No" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }

}