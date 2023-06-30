#include<bits/stdc++.h>
using namespace std;
int fun(string s,int k){
    map<char,int> m;
    int n=s.size();
    if(n==0)return 0;
    for(int i=0;i<n;i++)m[s[i]]++;
    int i=0;
    while(i<n and m[s[i]]>=k)i++;
    if(i==n)return n;
    return max(fun(s.substr(0,i),k),fun(s.substr(i+1,n-i-1),k));
}
int main() {
    int k; string s;
    cin>>k>>s;
    cout<<fun(s,k);
    return 0;
}
