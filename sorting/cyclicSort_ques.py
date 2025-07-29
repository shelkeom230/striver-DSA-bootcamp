# all cyclic sort questions from kunal lectures

import sys, threading

sys.stdout = open("basic maths/output.txt", "w")
sys.stdin = open("basic maths/input.txt", "r")


# Cyclic Sort
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        # calculate correct index
        correct_idx = arr[i] - 1

        # check if element is at correct index
        if arr[i] != arr[correct_idx]:
            # swap
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        else:
            # check for next index
            i += 1
    return arr


# Missing Number using Cyclic Sort
def missing_number(arr):
    n = len(arr)
    i = 0

    # run cyclic sort
    while i < n:
        correct_index = arr[i]  # correct index for any element is its value itself
        # if element is less than array size, then only consider it
        if arr[i] < n and arr[i] != arr[correct_index]:
            # swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # otherwise, go to next index
            i += 1

    # case 1 --> check if element and index are not equal
    for j in range(n):
        if arr[j] != j:
            return j

    # case 2 --> missing element is equal to n only
    return n


# Find All Numbers Disappeared in an Array
def find_all_missing_numbers(arr):
    n = len(arr)
    missing = []

    # apply cyclic sort
    i = 0
    while i < n:
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            # swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # move on to next index
            i += 1

    # push missing elements
    for j in range(n):
        if arr[j] != j + 1:
            missing.append(j + 1)

    return missing


# Find the Duplicate Number
def find_duplicate(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            # swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # move on to next index
            i += 1

    # find duplicate number
    for j in range(n):
        if arr[j] != j + 1:
            return arr[j]
    return -1  # in case no duplicate found (though problem states there is one)


# Find All Duplicates
def find_all_duplicates(arr):
    n = len(arr)
    duplicates = []
    i = 0

    # run cyclic sort
    while i < n:
        if arr[i] != arr[arr[i] - 1]:
            correct_index = arr[i] - 1
            # swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # move on to next index
            i += 1

    # find all duplicates
    for j in range(n):
        if arr[j] != j + 1:
            duplicates.append(arr[j])
    return duplicates


# Set Mismatch - finding duplicate and missing number
def set_mismatch(arr):
    n = len(arr)
    i = 0

    while i < n:
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            # swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # move on to next index
            i += 1

    # find the answers
    dup, missing = -1, -1
    for j in range(n):
        if arr[j] != j + 1:
            # dup
            dup = arr[j]
            # missing
            missing = j + 1
        if dup != -1 and missing != -1:
            break
    return [dup, missing]


# First Missing Positive - find the first missing +ve number from an unsorted array
def first_missing_positive(arr):
    n = len(arr)
    i = 0

    while i < n:
        correct_index = arr[i] - 1
        # Only consider numbers in range [1, n]
        if 0 <= arr[i] <= n and arr[i] != arr[correct_index]:
            # swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # move on to next index
            i += 1

    # find the first missing positive here
    for j in range(n):
        if arr[j] != j + 1:
            return j + 1

    # corner case --> if all are present in [1..N], then return n+1
    return n + 1


# Quick Sort
def quick_sort(arr, low, hi):
    # base case
    if low >= hi:
        return

    # take 2 pointers
    start = low
    end = hi
    mid = start + (end - start) // 2
    pivot = arr[mid]

    while start <= end:
        # move start until you find first element greater than pivot
        while arr[start] < pivot:
            start += 1

        # reduce end until you find first element less than pivot
        while arr[end] > pivot:
            end -= 1

        # if start <= end, swap to remove violations
        if start <= end:
            # swap
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # now pivot is at its correct index, sort the halves now
    quick_sort(arr, low, end)
    quick_sort(arr, start, hi)


def main():
    sys.stdin = open("sorting/input.txt", "r")
    sys.stdout = open("sorting/output.txt", "w")
    input = sys.stdin.readline

    # input here
    n = int(input())
    arr = list(map(int, input().split(",")))
    quick_sort(arr, 0, n - 1)
    print(arr)


threading.Thread(target=main).start()
