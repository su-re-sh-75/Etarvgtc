#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	// taking test case as input
	cin>>t;
	while(t--){
		int n;

		cin>>n;
		int a[n];

		for(int i = 0 ;i<n;i++){
			cin>>a[i];
		}


		for(int i = 0;i<n;i++){
			a[i] = a[i] + a[a[i]] * n;
		}
        for(int i = 0; i < n; i++)
            a[i] = a[i] * 1.0 / n;
            
		for(int i = 0;i<n;i++)
			cout<<a[i]<<" ";
		cout<<"\n";
	}
}