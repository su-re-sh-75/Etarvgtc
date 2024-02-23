'''
Polynomial Multiplication Using Divide and Conquer 
(3 Multiplications instead of 4)
Time Complexity: O(n^log3) or O(n^1.58)
'''

import random

def multiply_polynomial_test(poly1, poly2):
    
    degree = len(poly1) + len(poly2) - 1
    product = [0] * degree

    
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            product[i + j] += poly1[i] * poly2[j]

    return product

def generate_test_case():
    m = random.randint(50, 100)  
    n = random.randint(50, 100)
    poly1 = [random.randint(10, 50) for _ in range(m)]
    poly2 = [random.randint(10, 50) for _ in range(n)]

    return m, n, poly1, poly2


def remove_zeros(items):
    non_zero_items = []
    
    for ele in items:
        if ele != 0:
            non_zero_items.append(ele)
    
    return non_zero_items

def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

def subtract(poly1, poly2):
    poly = [-i for i in poly2]
    return add(poly1,poly)

def multiply_polynomial(poly1, poly2, m, n):
    if m == 0 or n == 0:
        return []
    
    if m == 1:
        if poly1[0] == 0:
            return [0]
        else:
            return [poly1[0] * i for i in poly2]
    elif n == 1:
        if poly2[0] == 0:
            return [0]
        else:
            return [poly2[0] * i for i in poly1]
    
    n = max(m,n)
    
    if n%2 != 0:
        n = n -1
    
    # print(n)
    
    A, B = split(poly1,poly2)
    add_A = add(A[0], A[1])
    add_B = add(B[0], B[1])
    Y = multiply_polynomial(add_A, add_B, len(add_A), len(add_B))
    U = multiply_polynomial(A[0], B[0], len(A[0]), len(B[0]))
    Z = multiply_polynomial(A[1], B[1], len(A[1]), len(B[1]))
    # print('Before:')
    # print(Y, U, Z)
    
    Y = increase_exponent(subtract(Y, add(U, Z)), n //2)
    Z = increase_exponent(Z, n)
    
    # print('After:')
    # print(Y, U, Z)
    
    result = add(Y, add(U, Z))
    result = remove_zeros(result)
    return result

def main():
    # Generate test cases
    num_test_cases = 1
    for i in range(num_test_cases):
        # m, n, poly1, poly2 = generate_test_case()
        m , n = 88, 77
        lst1 = "15 33 42 33 33 29 45 49 26 25 12 40 34 45 45 40 42 11 27 15 20 36 28 27 27 41 20 48 24 18 29 48 15 49 27 12 22 20 19 12 45 30 27 32 37 24 23 32 43 42 46 42 33 39 25 19 22 23 27 40 29 35 29 40 13 11 14 12 28 30 37 44 43 18 19 44 46 12 22 26 11 22 44 11 46 24 11 45"
        lst2 = "27 14 27 25 45 20 49 43 37 20 29 11 27 40 31 24 47 28 20 37 11 34 16 41 16 24 19 35 37 11 48 40 29 43 16 20 34 24 48 17 28 13 10 24 31 28 29 33 35 11 26 10 44 36 39 13 44 18 46 15 27 21 41 39 48 37 25 27 22 49 21 21 26 44 35 34 27"
        lst3 = "405 1101 2001 2745 3987 4971 6622 8148 9505 10396 10891 11701 11896 13695 14668 16029 16603 17737 18953 19984 20719 20887 21317 21469 21720 22962 22737 24976 26285 27129 27796 29224 29508 30862 32613 32404 31306 35179 33718 35523 35720 35928 35179 36980 39215 37594 40793 40383 41181 42467 43791 43697 45966 46102 49179 47841 49628 50232 51506 53286 52914 54538 52042 56905 56520 58406 58269 59366 58638 60806 60560 62655 61410 61920 64330 66749 68963 68474 69447 68331 67286 66245 64990 64883 64620 65431 64608 65952 65244 65374 61886 62250 58651 57202 58528 56463 56523 55642 55121 53441 54239 52174 51118 52012 48536 49160 50328 48125 46227 46365 43470 42409 43746 42997 43521 44275 41081 41567 38401 37714 37459 35006 36461 35720 34429 33601 31140 30118 29722 27556 27018 26167 27492 25312 26533 24681 23476 22841 21822 21073 20927 18997 17910 18406 18245 18532 15942 15355 14441 13630 12160 12316 9375 8397 7805 7067 7205 6299 5459 4355 4423 2597 1827 1215"
        poly1 = list(map(int, lst1.split(" ")))
        poly2 = list(map(int, lst2.split(" ")))
        product = list(map(int, lst3.split(" ")))
        result = multiply_polynomial(poly1, poly2, m, n)
        if result == product:
            print("Test Passed", i+1)
            print(f"{m} {n}")
            print()
            print(" ".join(map(str, poly1)))
            print()
            print(" ".join(map(str, poly2)))
            print()
            print(" ".join(map(str, result)))
            print()

if __name__ == "__main__":
    main()