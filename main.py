#!/usr/bin/env python

def findMax(arr, int k) -> int:
    if(n < 2): 
        return 0
    if(n == 2):
        return arr[1] - arr[0]
    max_num = 0
    for i in range(k, arr.len()):
        res = arr[i] - arr[k]
        if (res > max_num):
            max_num = res
    return max(max_num, findMax(arr, k+1))


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(best(arr))


if __name__ == "__main__":
    main()
