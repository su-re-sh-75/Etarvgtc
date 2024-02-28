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

*Writing your own solution / logic is not allowed. Perform
the task given below by fixing the buggy code.
Identify the logical errors in the code to get to the
solution.*

> Expected Time Complexity: o(n)
</p>

<h3>Input:</h3>
<p>
The first line contains an integer N, denoting the size of the array. 

The second line contains N space separated integers denoting the values arr[i] of the array.
</p>

<h3>Output:</h3>
<p>
Elements of the modified array separated by spaces.
</p>

<details>
<summary>Constraints:</summary>

```
1 <= N <= 100
0 <= arr[i] <= N-1
```
</details><br>

<h3>Example:</h3>
<h3>Sample Input: 1</h3>
6 <br>
0 5 1 2 4 3 <br>

<h3>Sample Output: 1</h3>
0 3 5 1 4 2 <br>

<h3>Sample Input: 2</h3>
5 <br>
4 3 2 1 0 <br>

<h3>Sample Output: 2</h3>
0 1 2 3 4 <br>

<details>
<summary>DSL Code Stub:</summary>

```
function(integer_array, rearrange, integer_array arr, integer n)

integer(n)

array(integer, arr, n, single)

invoke(integer_array, result, rearrange, arr, n)

print(integer_array,result)
```
</details><br>


## Question 2: BST Deletion

[GFG Theory Ref](https://www.geeksforgeeks.org/multiply-two-polynomials-2/)

<h3>Problem Statement:</h3>
<p>
Given a Binary Search Tree (BST) and a key value,  debug the function to delete the node containing the given key from the BST while maintaining the properties of a BST.

> Expected Time complexity: O(log n)
>
> Expected Space Complexity: O(1)


*Writing your own solution / logic is not allowed. Perform
the task given below by fixing the buggy code.
Identify the logical errors in the code to get to the
solution.*
</p>

<h3>Input:</h3>
<p>
The first line contains an integer key, which need to be deleted.

The second line contains an integer n, denoting the number of nodes. 

The next n lines contains node value in the order of insertion.

</p>

<h3>Output:</h3>
<p>
Inorder Traversal of modified Tree - space separated.
</p>

<details>
<summary>Constraints:</summary>
none
</details>

<h3>Example:</h3>
<h3>Sample Input 1: Also test case 1 (Tag: Present in Tree)</h3>

```
15
5
5
15
3
8
12
```
<h3>Sample Output:</h3>
3 5 8 12
<br>
<h3>Sample Input 2: Also test case 2 (Tag: Not in Tree)</h3>

```
7
6
10
3
8
12
15
20
```
<h3>Sample Output:</h3>
3 8 10 12 15 20
<br>


<details>
<summary> DSL Code Stub</summary>

```
function(integer_binary_search_tree, delete_node, integer_binary_search_tree t, integer key)

integer(key)

integer_binary_search_tree(t)

invoke(integer_binary_search_tree, result_tree, delete_node, t, key)

print(integer_binary_search_tree, result_tree)
```
</details><br>

<details>
<summary> HiddenTest Case: 1 </summary>

```
10
4
15
3
8
12

3 8 12 15
```
</details><br>
<details>
<summary> Hidden Test Case: 2 </summary>

```
45
15
10
15
21
35
37
40
50
55
60
65
70
75
80
90
53

10 15 21 35 37 40 50 53 55 60 65 70 75 80 90
```
</details><br>
<details>
<summary> Hidden Test Case: 3 </summary>

```
56
0

none
```
</details><br>
<details>
<summary> Hidden Test Case: 4 </summary>

```
10
15
10
14
5
15
3
8
12
18
1
7
9
11
13
17
20

1 3 5 7 8 9 11 12 13 14 15 17 18 20
```
</details><br>
<details>
<summary> Hidden Test Case: 5 </summary>

```
70
12
50
25
10
5
15
30
75
60
70
90
80
85

5 10 15 25 30 50 60 75 80 85 90
```
</details><br>
<details>
<summary> Hidden Test Case: 6 </summary>

```
3
11
8
3
1
5
7
12
10
9
11
15
18

1 5 7 8 9 10 11 12 15 18
```
</details>