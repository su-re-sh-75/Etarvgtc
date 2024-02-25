#include <bits/stdc++.h>
using namespace std;

void rearrange(int *arr, int n) {
	
	for(int i = 0; i < n; i++)
		arr[i] = arr[i] + arr[arr[i]] * n;
		
	for(int i = 0; i < n; i++)
		arr[i] = arr[i] * 1.0 / n;
}

int main(){
	int n;
	cin>>n;

	int a[n];
	for(int i = 0;i<n;i++){
		cin>>a[i];
	}

	rearrange(a,n);
		
	for(int i = 0;i<n;i++)
		cout<<a[i]<<" ";
	cout<<"\n";
}