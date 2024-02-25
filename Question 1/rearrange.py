#!/bin/python3

def rearrange(arr, n):
    '''temp = [0] * n

    for i in range(n):
        temp[i] = arr[arr[i]]

    for i in range(n):
        arr[i] = temp[i]
    '''
    
    for i in range(n):
        arr[i] = arr[i] + (arr[arr[i]]%n) * n

    for i in range(n):
        arr[i] //= n

    return arr

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    result = rearrange(arr, n)

    print(result)
