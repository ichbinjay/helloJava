#include <iostream>
using namespace std;

void pattern(int l, int c){
	for(int i=0;i<l;i++){
		for(int j=0;j<c;j++){
			if(i==0 ||i==l-1)
				cout<<"*";
			else{
				if(j==0 || j==c-1){
					cout<<"*";
				}
				else{
					cout<<".";
				}
			}
		}
		cout<<endl;
	}
}

int main() {
	
	// your code here
	int t,l,c;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>l>>c;
		pattern(l,c);
		cout<<endl;
	}

	return 0;
}