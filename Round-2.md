<h1 align='center'> Round 2 Code Editing</h1>

[Hackerrank support for creating qns, testcases](https://support.hackerrank.com/hc/en-us/articles/223080547-Creating-a-Custom-Checker)

## Question 1: Rearrange Geek and his Classmates

[Reference. See Qn 2](https://practice.geeksforgeeks.org/contest/debugging/problems)

[Buggy code - cpp](https://ide.geeksforgeeks.org/PFWYVCLkbp)

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

Writing your own solution / logic is not allowed. Perform
the task given below by fixing the buggy code.
Identify the logical errors in the code to get to the
solution.

>Expected Time Complexity: o(n)
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

## Question 2: Polynomial Multiplication

[GFG Theory Ref](https://www.geeksforgeeks.org/multiply-two-polynomials-2/)

[YT Divide and Conquer](https://www.youtube.com/watch?v=6eFWMhS_PTA)

[GFG Practice: normal](https://www.geeksforgeeks.org/problems/multiply-two-polynomals0721/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

[Python code ref](https://jovian.com/indexkyou/python-divide-and-conquer-assignment)

<h3>Problem Statement:</h3>
<p>
Given two polynomials represented by two arrays that contains the coefficients of poynomials, return the polynomial in form of array formed after multiplication of given polynomials.

> For example, the arrays `[2, 0, 5, 7]` and `[3, 4, 2]` represent the polynomials $2 + 5x^2 + 7x^3$ and $3 + 4x + 2x^2$. 
> 
> Their product is 
>
> $(2 \times 3) + (2 \times 4 + 0 \times 3)x + (2 \times 2 + 3 \times 5 + 4 \times 0)x^2 + $
> $(7 \times 3 + 5 \times 4 + 0 \times 2)x^3 + (7 \times 4 + 5 \times 2)x^4 + (7 \times 2)x^5$ 
> 
> i.e. 
>
>$6 + 8x + 19x^2 + 41x^3 + 38x^4 + 14x^5$
> 
>It can be represented by the list `[6, 8, 19, 41, 38, 14]`.

Writing your own solution / logic is not allowed. Perform
the task given below by fixing the buggy code.
Identify the logical errors in the code to get to the
solution.

>Expected Time Complexity: O(n<sup>log3</sup>) or O(n<sup>1.58</sup>)
</p>

<h3>Input:</h3>
<p>
The first line of the input contains an array poly1 of size M indicating Polynomial 1.
<br>
The second line of the input contains an array poly2 of size N indicating Polynomial 2.
</p>

<h3>Output:</h3>
<p>
An array indicating Product of Polynomial 1 and 2.
</p>

<details>
<summary>Constraints:</summary>

``` 
1 ≤ M, N ≤ 100

1 ≤  poly1[i] , poly2[i]  ≤ 100
```
</details><br>

<h3>Example:</h3>
<h3>Sample Input:</h3>
[2, 0, 5, 7] <br>
[3, 4, 2] <br>

<h3>Sample Output:</h3>
[6, 8, 19, 41, 38, 14] <br>
<br>


<details>
<summary> DSL Code Stub</summary>

```
function(integer_array, multiply_polynomial, integer_array poly1, integer_array poly2, integer m, integer n)

integer(m) integer(n)

array(integer, poly1, m, single)

array(integer, poly2, n, single)

invoke(integer_array, product, multiply_polynomial, poly1, poly2, m, n)

print(integer_array,product)
```
</details><br>
