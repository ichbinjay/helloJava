#include <iostream>
using namespace std;

int main()
{
    int n;
    string s;
    cin >> n;
    while (n--)
    {
        cin >> s;
        int l = s.length();
        if(l>=11)
        {
            cout << s[0] <<l- 2 << s[l-1];
        }
        else
        {
            cout << s;
        }
        cout << "\n";
    }
    return 0;
}