#include <iostream>
#include <vector>
using namespace std;

vector<int> rearrange(vector<int> arr, int n) {
    /*int temp[n];
    for (int i = 0; i < n; i++) {
        temp[i] = arr[arr[i]];
    }

    for (int i = 0; i < n; i++) {
        arr[i] = temp[i];
    }*/
	for(int i = 0; i < n; i++)
		arr[i] = arr[i] + (arr[arr[i]]%n) * n;
		
	for(int i = 0; i < n; i++)
		arr[i] = arr[i] * 1.0 / n;
    return arr;
}

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> result = rearrange(arr, n);

    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }

    return 0;
}
