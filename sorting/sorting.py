import sys

sys.stdout = open("sorting/output.txt", "w")
sys.stdin = open("sorting/input.txt", "r")


def bubbleSort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort2(arr):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort3(arr):
    # if no swap occurs, then break the loop
    isSwap = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSwap += 1

        if isSwap == 0:
            break
    return arr


def selection_sort(arr, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


def insertion_sort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def merge(arr, low, mid, high):
    left, right = low, mid + 1
    tmp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1

    while left <= mid:
        tmp.append(arr[left])
        left += 1

    while right <= high:
        tmp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = tmp[i - low]


def merge_sort(arr, low, high):
    if low <= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    return arr


def part(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:

        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] >= pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pidx = part(arr, low, high)
        quick_sort(arr, low, pidx - 1)
        quick_sort(arr, pidx + 1, high)
    return arr


def rec_bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    rec_bubble_sort(arr, n - 1)


# quick sort easier implementation
def quickSort(arr, low, hi):
    # base case
    if low >= hi:
        return

    # take 2 pointers
    start, end = low, hi

    # calculate mid index
    mid = (start + end) // 2
    # take mid element as pivot for best case nlogn
    pivot = arr[mid]

    while start <= end:
        # move start until you find first element greater than pivot
        while arr[start] < pivot:
            start += 1

        # move end until you find first element less than pivot
        while arr[end] > pivot:
            end -= 1

        # if start<=end , swap to remove voilations
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # now pivot is at it's correct index, sort the halves now
    quickSort(arr, low, end)
    quickSort(arr, start, hi)


# cyclic sort
def cyclicSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        # calculate correct index
        corrIdx = arr[i] - 1

        # check if element is at correct index
        if arr[i] != arr[corrIdx]:
            # swap
            arr[i], arr[corrIdx] = arr[corrIdx], arr[i]
        else:
            # check for next index
            i += 1


def rec_insertion_sort(arr, i, n):

    if i == n:
        return

    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]

    rec_insertion_sort(arr, i + 1, n)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(",")))
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
