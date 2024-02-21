<h1 align='center'> Round 2 Code Editing</h1>

## Question 1: Rearrange Geek and his Classmates

[Reference Link. See Qn 2](https://practice.geeksforgeeks.org/contest/debugging/problems)

[Buggy code - cpp](https://ide.geeksforgeeks.org/PFWYVCLkbp)

<details>
<summary>Debugging Instructions:</summary>
Writing your own solution / logic is not allowed. Perform
the task given below by fixing the buggy code.
Identify the logical errors in the code to get to the
solution.
</details><br>

<h3>Problem Statement:</h3>
<p>
Geek and his classmates are playing a prank on their
Computer Science teacher. They change places
every time the teacher turns to look at the
blackboard.

Each of the N students in the class can be identified
by a unique roll number X and each desk has a
number i associated with it. Only one student can sit
on one desk.

Each time the teacher turns her back, a student with
roll number X sitting on desk number i gets up and
takes the place of the student with roll number i.

If the current position of N students in the class is
given to you in an array, such that i is the desk
number and a[i] is the roll number of the student
sitting on the desk, can you modify a[] to represent
the next position of all the students ?
</p>

<h3>Input:</h3>
<p>
The first line of the input contains an integer T denoting the number of testcases. The first line of
each test case contains an integer N, denoting the size of the array. The second line of each test
case contains N space separated integers denoting the values arr[i] of the array.</p>

<h3>Output:</h3>
<p>
For each test case, in a new line, print the elements of the modified array separated by spaces.
</p>

<details>
<summary>Constraints:</summary>

``` 1 <= T <= 10 
1 <= N <= 10^5 
0 <= arr[i] <= N-1
```
</details><br>

<h3>Example:</h3>
<h3>Sample Input:</h3>
2 <br>
6 <br>
051243 <br>
5 <br>
43210 <br>

<h3>Sample Output:</h3>
035142 <br>
01234 <br>

<details>
<summary>Buggy Code: c++</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	// taking test case as input
	cin>>t;
	while(t--){
		int n;
		// taking n - size of array as input
		cin>>n;
		int a[n];
		// taking input for the array
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
```
</details><br>

<details>
<summary>Correct Answer 1:</summary>

```cpp
#include <iostream>
using namespace std;

int main(){
	int t;
	// taking test case as input
	cin>>t;
	while(t--){
		int n;
		// taking n - size of array as input
		cin>>n;
		int a[n];
		// taking input for the array
		for(int i = 0 ;i<n;i++){
			cin>>a[i];
		}


		for(int i=0; i<n; i++){
		   a[i] = a[i] + (a[a[i] % n] % n) * n;	
		    
		}
		
		
        for(int i = 0; i < n; i++)
                a[i]= a[i] * 1 / n;
            
            
            
		for(int i = 0;i<n;i++)
			cout<<a[i]<<" ";
		cout<<"\n";
	}
}
```
</details><br>

<details>
<summary>Correct Answer 2:</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	// taking test case as input
	cin>>t;
	while(t--){
		int n;
		// taking n - size of array as input
		cin>>n;
		int a[n], b[n];
		// taking input for the array
		for(int i = 0 ;i<n;i++){
			cin>>a[i];
		}


		for(int i = 0;i<n;i++){
			b[i] = a[a[i]];
		}
        for(int i = 0; i < n; i++)
            a[i] = a[i] * 1.0 / n;
            
		for(int i = 0;i<n;i++)
			cout<<b[i]<<" ";
		cout<<"\n";
	}
}
```
</details><br>

<details>
<summary>Correct Answer 3:</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	// taking test case as input
	cin>>t;
	while(t--){
		int n;
		// taking n - size of array as input
		cin>>n;
		int a[n];
		// taking input for the array
		for(int i = 0 ;i<n;i++){
			cin>>a[i];
		}


		for(int i = 0;i<n;i++){
			a[i] = a[i] + (a[a[i]]%n) * n;
		}
		for(int i = 0;i<n;i++)
			cout<<a[i]/n<<" ";
		cout<<"\n";
	}
}
```
</details><br>

<details>
<summary>Correct Answer 4:</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	// taking test case as input
	cin>>t;
	while(t--){
		int n;
		// taking n - size of array as input
		cin>>n;
		int a[n];
		// taking input for the array
		for(int i = 0 ;i<n;i++){
			cin>>a[i];
		}

		for(int i = 0;i<n;i++){
			a[i] = a[i]+(a[a[i]]%n)*n;
			// 5 + 3*n
		}
        for(int i = 0; i < n; i++)
            a[i] = a[i] * 1.0 / n;
            
		for(int i = 0;i<n;i++)
			cout<<a[i]<<" ";
		cout<<"\n";
	}
}
```
</details><br>
