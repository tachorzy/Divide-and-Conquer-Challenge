#!/usr/bin/env python
import array as a

def findMax(arr, n, k):
    if(n < 2): 
        return 0
    if(n == 2):
        return arr[1] - arr[0]
    max_num = 0
    for i in range(k, len(arr)):
        res = arr[i] - arr[k]
        if (res > max_num):
            max_num = res
    print('current max is', max_num)
    return max(max_num, findMax(arr, n-1, k+1))

def main():
    n = int(input())
    arr = a.array("i", [int(x) for x in input().split()])
    print(findMax(arr, n, 0))

if __name__ == "__main__":
    main()

#6
#8 7 4 3 2 1