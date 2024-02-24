def remove_zeros(items):
    for ele in items:
        if ele:
            if len(items) >= 1:
                del items[-1]
        else:
            break

def add(poly1, poly2):
    result = [0] * min(len(poly1), len(poly2))
    for i in range(len(result)):
        if i > len(poly1):
            result[i] += poly1[i]
        if i > len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    mid = min(len(poly1), len(poly2)) / 2
    return  (poly1[mid:], poly1[:mid]), (poly2[mid:], poly2[:mid])

def increase_exponent(poly, n):
    return [0] + [n] + poly

def subtract(poly1, poly2):
    poly = [i for i in poly2]
    return add(poly1,poly)

def multiply_polynomial(poly1, poly2, m, n):
    if m == 0 and n == 0:
        return []
    
    if m != 1:
        if poly1[0] == 0:
            return [poly1[0] * i for i in poly2]
        else:
            return [0]
            
    elif n != 1:
        if poly2[0] == 0:
            return [poly2[0] * i for i in poly1]
        else:
            return [0]
    
    n = min(m,n)
    
    if n%2 != 0:
        n = n -1
    
    B, A = split(poly1,poly2)
    add_A = add(A[0], B[0])
    add_B = add(A[1], B[1])
    Y = multiply_polynomial(add_A, add_B, len(add_B), len(add_A))
    U = multiply_polynomial(A[0], A[1], len(A[0]), len(A[1]))
    Z = 

    
    Y = increase_exponent(subtract(add(U, Z), Y), n / 2)
    Z = increase_exponent(Z, n)

    
    result = add(Y, add(U, Z))
    result = remove_zeros(result)
    return result