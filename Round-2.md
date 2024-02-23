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

<details>
<summary> Sample Test Case: 1 </summary>

```
4 3
2 0 5 7
3 4 2

6 8 19 41 38 14
```
</details><br>
<details>
<summary> Sample Test Case: 2 </summary>

```
4 3
1 0 3 2
2 0 4

2 0 10 4 12 8
```
</details><br>
<details>
<summary> Hidden Test Case: 3 </summary>

```
5 4
1 9 3 4 7
4 0 2 5

4 36 14 39 79 23 34 35
```
</details><br>
<details>
<summary> Hidden Test Case: 4 </summary>

```
3 3
0 0 0
3 4 2

0 0 0 0 0
```
</details><br>
<details>
<summary> Hidden Test Case: 5 </summary>

```
3 2
0 0 0
0 0

0 0 0
```
</details><br>
<details>
<summary> Hidden Test Case: 6 </summary>

```
5 4
2 0 5 7 5
3 4 2 1

6 8 19 43 53 39 17 5
```
</details><br>
<details>
<summary> Hidden Test Case: 7 </summary>

```
5 3
2 0 5 0 0
3 4 2

6 8 19 20 10
```
</details><br>

<details>
<summary> Hard Test Case: 1 </summary>

```
66 90

46 20 28 26 19 41 17 38 28 41 44 20 30 41 44 18 14 23 37 25 42 36 45 36 18 36 41 10 16 40 37 48 48 21 16 23 23 13 20 32 17 31 38 11 30 31 19 27 29 29 44 41 24 26 25 31 27 14 10 40 47 16 35 21 29 41

46 24 39 26 46 21 45 41 39 44 27 39 41 48 21 21 24 24 14 42 31 33 14 19 40 49 14 19 27 42 19 23 38 11 45 18 42 17 37 50 12 23 15 37 14 15 14 31 47 42 31 18 37 24 30 29 35 14 46 27 49 23 46 25 27 27 23 29 41 23 32 25 10 41 40 41 13 16 14 19 32 44 31 18 21 13 18 43 11 25

2116 2024 3562 3844 5226 5970 6961 8819 9223 11889 11866 13612 14481 16668 17469 16974 18280 18291 19487 20183 22021 23040 23965 23640 25151 26772 27898 26896 27178 30287 30265 31427 33632 33517 35371 33686 34311 35012 37149 39133 34685 38808 39167 39943 39620 40068 40303 40048 43401 43155 45811 46172 46934 46890 48481 49162 50486 51454 51073 52201 55079 55624 55913 56410 56427 57707 56695 57702 58744 58684 58505 57571 56488 57393 56953 56681 54906 53584 56028 54483 56825 55629 54130 54756 56585 53916 52040 54624 54325 55176 52519 51750 50143 50281 51569 46873 47570 46087 45935 46643 44291 43303 41595 42248 40559 38592 38386 38360 36618 36784 35777 34863 36185 34463 31997 31092 29377 29138 29406 28296 27150 25576 24948 24468 23510 22871 21231 20467 19943 19321 18648 17639 16854 16846 15637 14942 13430 13163 12429 11446 10841 9120 8598 8028 7365 6795 7050 5688 4455 4472 2743 3091 2607 1176 1025
```
</details><br>

<details>
<summary> Hard Test Case: 2 </summary>

```
77 75

14 25 11 43 29 30 17 16 41 12 40 22 29 24 18 38 28 29 14 22 36 44 49 18 27 14 44 24 37 22 39 17 26 42 12 36 30 38 35 13 39 18 24 28 17 15 32 19 27 19 11 15 11 12 28 20 17 50 31 26 27 35 50 10 33 42 15 50 48 34 10 14 36 48 23 32 20

22 34 43 50 50 48 26 21 42 32 11 23 24 27 46 11 22 42 18 50 20 22 33 14 50 42 48 19 40 42 19 21 35 23 43 10 23 27 35 30 23 14 37 27 41 33 15 13 40 17 45 28 23 42 43 25 23 27 15 33 16 12 24 28 40 27 24 50 12 22 41 31 18 15 33

308 1026 1694 3095 4523 5967 6905 7292 8590 8935 9214 10170 11222 11693 12102 12969 13737 15251 15118 15983 17126 17424 20073 19761 22065 22774 22572 24882 24315 28058 27284 27143 28635 28762 31216 30732 31672 32433 33341 34647 35447 36692 35935 36074 37317 38377 39215 39411 39271 40452 40541 40649 41810 40321 44375 42761 43209 44671 45736 47420 48627 47972 50961 49283 51483 53567 53243 53879 54147 55669 58531 57400 58338 57224 60452 60080 60433 58728 57582 56591 55442 56021 53305 52255 51718 51025 53479 50242 48845 48542 48413 48612 46769 46846 44963 42601 43251 42108 39671 40937 40113 38700 37895 34473 34805 34118 32780 34296 29967 30659 31306 29994 29710 27746 26056 26256 25464 25403 24657 23023 22467 23292 21224 20811 21288 19764 20302 19511 19162 18314 15785 17407 16569 13284 13609 13414 12345 10940 11531 11194 8929 7692 7596 6498 4563 4331 4134 3125 1599 1356 660

```
</details><br>

<details>
<summary> Hard Test Case: 3 </summary>

```
59 81

22 33 40 30 45 24 26 16 11 42 49 49 39 29 20 43 41 25 33 14 37 33 37 25 41 15 31 41 42 29 37 43 37 16 28 32 24 20 47 23 13 39 24 33 22 34 33 50 10 30 33 30 47 10 21 20 14 25 44

15 12 24 47 32 13 43 38 23 50 22 31 16 34 10 20 33 29 31 44 25 49 47 18 40 10 44 14 42 18 45 38 20 36 40 19 20 20 42 29 24 42 24 38 31 38 43 25 35 31 43 47 43 41 45 23 29 17 48 21 16 49 31 17 19 36 46 31 44 49 49 17 48 19 36 18 33 22 17 39 35

330 759 1524 2756 4250 4842 5823 6978 7419 8390 9528 10538 11703 13523 12782 14044 14457 15658 17562 18761 19307 20398 22124 22449 23779 23720 24719 25407 27037 27082 30033 31690 31965 33594 34208 34739 33920 36459 36005 37372 37848 39559 39829 40667 42464 43014 43490 45098 46937 47284 49970 48919 51596 52305 55203 54119 55544 53896 56578 55129 57300 57586 58059 56598 56699 57595 55855 57410 57617 58706 57365 59866 58153 59618 58594 57424 59798 58367 58613 58643 59494 57706 57271 54634 54467 53172 51598 48930 51318 50369 49565 46633 47263 44497 42854 43127 44480 41821 39840 39891 39534 37423 35680 35866 34647 31729 31359 30775 30676 26985 27664 26037 24264 23359 21462 21872 20771 20260 18845 19038 16782 16564 14979 14660 14235 12071 12641 10550 8861 7523 7488 6163 5328 3434 3755 2639 2213 2591 1540

```
</details><br>
<details>
<summary> Hard Test Case: 4 </summary>

```
88 77

15 33 42 33 33 29 45 49 26 25 12 40 34 45 45 40 42 11 27 15 20 36 28 27 27 41 20 48 24 18 29 48 15 49 27 12 22 20 19 12 45 30 27 32 37 24 23 32 43 42 46 42 33 39 25 19 22 23 27 40 29 35 29 40 13 11 14 12 28 30 37 44 43 18 19 44 46 12 22 26 11 22 44 11 46 24 11 45

27 14 27 25 45 20 49 43 37 20 29 11 27 40 31 24 47 28 20 37 11 34 16 41 16 24 19 35 37 11 48 40 29 43 16 20 34 24 48 17 28 13 10 24 31 28 29 33 35 11 26 10 44 36 39 13 44 18 46 15 27 21 41 39 48 37 25 27 22 49 21 21 26 44 35 34 27

405 1101 2001 2745 3987 4971 6622 8148 9505 10396 10891 11701 11896 13695 14668 16029 16603 17737 18953 19984 20719 20887 21317 21469 21720 22962 22737 24976 26285 27129 27796 29224 29508 30862 32613 32404 31306 35179 33718 35523 35720 35928 35179 36980 39215 37594 40793 40383 41181 42467 43791 43697 45966 46102 49179 47841 49628 50232 51506 53286 52914 54538 52042 56905 56520 58406 58269 59366 58638 60806 60560 62655 61410 61920 64330 66749 68963 68474 69447 68331 67286 66245 64990 64883 64620 65431 64608 65952 65244 65374 61886 62250 58651 57202 58528 56463 56523 55642 55121 53441 54239 52174 51118 52012 48536 49160 50328 48125 46227 46365 43470 42409 43746 42997 43521 44275 41081 41567 38401 37714 37459 35006 36461 35720 34429 33601 31140 30118 29722 27556 27018 26167 27492 25312 26533 24681 23476 22841 21822 21073 20927 18997 17910 18406 18245 18532 15942 15355 14441 13630 12160 12316 9375 8397 7805 7067 7205 6299 5459 4355 4423 2597 1827 1215

```
</details><br>
<details>
<summary> Hard Test Case: 5 </summary>

```
100 100

45 27 33 28 35 23 13 32 16 50 22 38 43 24 12 28 36 38 33 20 36 20 20 49 34 47 46 23 43 44 21 48 12 12 37 19 45 41 27 44 11 44 19 45 14 35 31 35 21 29 41 40 27 14 25 34 10 41 44 34 20 50 27 37 16 50 47 35 20 14 49 23 42 32 45 30 35 29 26 28 25 18 12 45 25 16 12 39 38 38 23 26 34 24 41 14 47 37 21 47

35 35 15 16 14 32 17 35 50 16 28 50 44 33 41 19 29 50 35 18 35 31 25 29 48 35 32 30 18 36 34 26 49 29 34 14 45 21 28 39 44 39 33 45 21 37 29 40 46 11 23 23 45 33 33 15 42 41 41 37 48 39 49 37 23 20 25 48 33 40 21 38 14 28 22 10 17 28 34 29 46 24 25 39 19 10 14 27 43 14 30 49 23 30 33 39 22 15 12 16


1575 2520 2775 3260 3762 4796 4324 5962 7385 8141 9107 10520 12691 12295 13399 13579 15207 17607 17598 17804 19742 20038 19873 22695 24136 25150 26350 26477 27933 29743 29641 31196 31887 33015 34901 33845 38194 37720 37100 39696 39760 42570 43190 44697 43654 45485 45572 47908 49880 49507 50694 51064 53334 52106 53751 55192 55119 57558 58767 60206 60739 62257 63517 66644 63768 66808 67577 68817 70780 71426 72240 74662 73334 74936 74776 76455 75399 78241 78869 80629 79361 80769 82934 84233 84973 82494 83185 85356 86396 86206 88186 90453 87463 88855 90354 93030 90887 95509 92365 95311 92592 90212 90641 91434 92195 90324 91356 88787 89109 85238 85529 83920 81761 82467 81341 78859 78717 79854 77023 79333 74921 74043 73031 71839 70896 68395 68754 65944 68080 65214 65757 62883 63150 61015 60711 60319 57854 57839 55604 55834 53727 53996 51172 49619 49613 49755 47961 44958 44534 44979 44869 42520 42511 42227 41728 39657 40677 38300 36696 34250 33909 33044 29938 29508 27950 28513 27320 26621 24483 22953 22988 21663 20009 18614 18930 18272 17909 17285 16325 16342 14450 13113 13999 12106 12010 11296 10741 11379 8913 8479 8079 6520 5666 4713 3638 2545 1549 900 752
```
</details><br>
