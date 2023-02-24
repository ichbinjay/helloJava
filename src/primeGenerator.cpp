
#include <iostream>
#include <cmath>

using namespace std;
int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int a, b;
        cin >> a >> b;
        for(int j = a; j <= b; j++){
            bool flag = false;
            for(int k = 2; k <= sqrt(j); k++){
                if(j % k == 0){
                    flag = true;
                    break;
                }
            }
            if(!flag && j != 1){
                cout << j << "\n";
            }
        }
        cout << "\n";
    }
}