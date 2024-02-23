'''
Polynomial Multiplication Using Divide and Conquer 
(3 Multiplications instead of 4)
Time Complexity: O(n^log3) or O(n^1.58)
'''

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
    
    Y = multiply_polynomial(add(A[0], A[1]), add(B[0], B[1]))
    U = multiply_polynomial(A[0], B[0])
    Z = multiply_polynomial(A[1], B[1])
    # print('Before:')
    # print(Y, U, Z)
    
    Y = increase_exponent(subtract(Y, add(U, Z)), n //2)
    Z = increase_exponent(Z, n)
    
    # print('After:')
    # print(Y, U, Z)
    
    result = add(Y, add(U, Z))
    result = remove_zeros(result)
    return result
    
print(multiply_polynomial([2, 0, 5, 7], [3, 4, 2], 4, 3))