#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int h,m; cin>>h>>m;
    double hd=(h*30.0)+m*0.5;
    double md=(m*6.0);
    double d=abs(hd-md);
    printf("%.5lf",min(d,360-d));
    return 0;
}
