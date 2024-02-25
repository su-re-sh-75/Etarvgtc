#include <stdio.h>

int* rearrange(int *arr, int n) {

    /*int temp[n];
    for (int i = 0; i < n; i++) {
        temp[i] = arr[arr[i]];
    }

    for (int i = 0; i < n; i++) {
        arr[i] = temp[i];
    }*/

	for(int i = 0; i < n; i++)
		arr[i] = arr[i] + arr[arr[i]] * n;
		
	for(int i = 0; i < n; i++)
		arr[i] = arr[i] * 1.0 / n;
    
	// *result_count = n;
    return arr;
}

int main(){
	int n;
	scanf("%d", &n);

	int a[n];
	for(int i = 0;i<n;i++){
		scanf("\n%d ", &a[i]);
	}

	rearrange(a,n);
		
    printf("\n");
	for(int i = 0;i<n;i++)
		printf("%d ", a[i]);
    printf("\n");
}