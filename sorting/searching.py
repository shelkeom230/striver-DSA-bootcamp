import sys, threading

sys.stdout = open("sorting/output.txt", "w")
sys.stdin = open("sorting/input.txt", "r")


# linear search brute
def linearSearchBrute(arr, key):
    n = len(arr)

    for i in range(n):
        if arr[i] == key:
            return i
    return -1


# linear search optimal -- stop when key is found
def linearSearchOptimal(arr, key):
    n = len(arr)

    idx = None
    for i in range(n):
        if key == arr[i]:
            idx = i
            break
    return idx if idx != None else -1


# binary search iterative
def binarySearchBrute(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# binary search recursive
def binarySearchRecursive(arr, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearchRecursive(arr, mid + 1, end, target)
    else:
        return binarySearchRecursive(arr, start, mid - 1, target)


if __name__ == "__main__":
    arr = list(map(int, input().split(",")))
    target = int(input())
    print(binarySearchRecursive(arr, 0, len(arr) - 1, target))
