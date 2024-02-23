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
    num_test_cases = 5
    for i in range(num_test_cases):
        m, n, poly1, poly2 = generate_test_case()
        product = multiply_polynomial_test(poly1, poly2)
        result = multiply_polynomial(poly1, poly2, m, n)
        if result == product:
            print("Test Passed", i+1)
            print(f"{m} {n}")
            print()
            print(" ".join(map(str, poly1)))
            print()
            print(" ".join(map(str, poly2)))
            print()
            print(" ".join(map(str, product)))
            print()

if __name__ == "__main__":
    main()