#!/usr/bin/env python

def calculateMin(arr, left, right):
    min = arr[left]
    for i in range(left, right+1):
        if arr[i] < min:
            min = arr[i]
    return min

def calculateMax(arr, left, right):
    max = arr[left]
    for i in range(left, right+1):
        if arr[i] > max:
            max = arr[i]
    return max 

def findMaxDifference(arr: list, left, right):
    if left >= right:
        return 0

    mid = (left + right)//2

    leftArray = findMaxDifference(arr, left, mid)
    rightArray = findMaxDifference(arr, mid+1, right)

    diff = max(arr[mid+1:]) - min(arr[left:mid+1])
    temp = max(max(leftArray, rightArray), diff)
    return temp


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(findMaxDifference(arr, 0, n-1))

if __name__ == "__main__":
    main()