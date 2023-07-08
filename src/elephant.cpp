//my solution
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,ans=0;
    cin>>n;
    while(n>0)
    {
        if(n>=5)
        {
            n-=5;
            ans++;
        }
        else if(n>=4)
        {
            n-=4;
            ans++;
        }
        else if(n>=3)
        {
            n-=3;
            ans++;
        }
        else if(n>=2)
        {
            n-=2;
            ans++;
        }
        else if(n>=1)
        {
            n-=1;
            ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
}

// saruarChy's solution
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,ans=0;
    int a[]={5,4,3,2,1};
    cin>>n;
    for(int i=0; i<5; i++)
    {
        ans+=n/a[i];
        n=n%a[i];
    }
    cout<<ans<<endl;
    return 0;
}