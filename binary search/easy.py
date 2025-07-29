import sys, threading


# binary search iterative
def binarySearchIterative(arr, target):
    n = len(arr)
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# binary search recursive
def binarySearchRecursive(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binarySearchRecursive(arr, target, start, mid - 1)
    else:
        return binarySearchRecursive(arr, target, mid + 1, end)


# Implement Lower Bound for an array -- optimal
def lowerBoundBrute(arr, x):
    n = len(arr)

    # base case
    if x > arr[n - 1]:
        return -1

    # linear search
    for i in range(n):
        if arr[i] >= x:
            return i


# Implement Lower Bound for an array -- optimal
# lower bound --> index of the first number greater than equal to target or x / smallest number greater than or equal to the target
def lowerBoundOptimal(arr, x):
    n = len(arr)
    ans = n
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= x:
            # mid can be possible answer
            ans = mid

            # also check for left half as well
            end = mid - 1
        else:
            start = mid + 1
    return ans


# implement upper bound -- brute force
# upper bound - greatest number less than equal to target
def upperBoundBrute(arr, x):
    n = len(arr)

    if x > arr[n - 1]:
        return -1
    ans = n
    for i in range(n):
        if arr[i] > x:
            ans = i
            break
    return ans


# implement upper bound -- optimal
def upperBoundOptimal(arr, x):
    n = len(arr)
    if x > arr[n - 1]:
        return -1
    ans = n
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > x:
            ans = mid

            end = mid - 1
        else:
            start = mid + 1
    return ans


# Search Insert Position -- brute force
def searchInsertPosBrute(arr, x):
    n = len(arr)
    ans = n
    for i in range(n):
        if arr[i] == x:
            ans = i
            return ans
        elif arr[i] > x:
            ans = i
            return ans
    return ans


# search insert position -- optimal approach
def searchInsertPosOptimal(arr, x):
    n = len(arr)
    ans = n

    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= x:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans


# find the floor and ceil of target in given array -- brute
def findFloorAndCeilBrute(arr, x):
    n = len(arr)
    floorele, ceilele = -1, -1

    if x > arr[n - 1] or x < arr[0]:
        return [-1, -1]

    for i in range(n):
        if arr[i] == x:
            floorele, ceilele = arr[i], arr[i]
            return [floorele, ceilele]
        elif arr[i] > x:
            floorele = arr[i - 1]
            ceilele = arr[i]
            return [floorele, ceilele]


# find the floor and ceil of target in given array -- optimal
def findFloorAndCeilOptimal(arr, x):
    n = len(arr)

    if x > arr[n - 1] or x < arr[0]:
        return [-1, -1]

    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return [arr[mid], arr[mid]]
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return (
        [arr[start], arr[end]] if arr[start] != -1 and arr[end] != -1 else [-1, -1]
    )  # [ceil,floor]


# find floor seprate code
def findFloor(arr, x):
    n = len(arr)
    ans = -1

    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= x:
            # mid value can be answer
            ans = arr[mid]

            # check right half also
            start = mid + 1
        else:
            end = mid - 1
    return ans


# find ceil seprate code
def findCeil(arr, x):
    n = len(arr)
    ans = -1

    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] >= x:
            ans = arr[mid]

            end = mid - 1
        else:
            start = mid + 1
    return ans


# Last occurrence in a sorted array -- brute - 0(N)
def lastOccurenceBrute(arr, x):
    n = len(arr)
    ans = -1

    for i in range(n - 1, -1, -1):
        if arr[i] == x:
            ans = i
            break
    return ans


# first occurence optimal approach
def firstOccurenceOptimal(arr, x):
    n = len(arr)

    ans = -1

    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] >= x:
            # maybe my answer
            ans = mid
            # check for right half also
            end = mid - 1
        else:
            start = mid + 1
    return ans


# last occurence optimal approach
def lastOccurenceOptimal(arr, x):
    n = len(arr)

    ans = -1

    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] <= x:
            # maybe my answer
            ans = mid
            # check for right half also
            start = mid + 1
        else:
            end = mid - 1
    return ans


# Search Element in a Rotated Sorted Array - brute force - simple linear search
def searchInRotatedSortedArray(arr, k):
    n = len(arr)
    for i in range(n):
        if arr[i] == k:
            return i
    return -1


# Search Element in a Rotated Sorted Array - optimal - binary search
def searchInRotatedSortedArrayOptimal(arr, k):
    n = len(arr)
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        # if target matches mid element , return mid index
        if arr[mid] == k:
            return mid

        # find out the sorted half
        # left sorted
        if arr[start] <= arr[mid]:
            # check if element present in left half
            if arr[start] <= k <= arr[mid]:
                # eliminate the right half
                end = mid - 1
            else:
                # eliminate the left half
                start = mid + 1

        # right sorted
        else:
            # check if element present in right half
            if arr[mid] <= k <= arr[end]:
                # eliminate the left half
                start = mid + 1
            else:
                # eliminate the right half
                end = mid - 1

    # element not present
    return -1


# count frequency in sorted array with duplicates - brute force - 0(N)
def countFreqArrayBruteForce(arr, target):
    count = 0
    for ele in arr:
        if ele == target:
            count += 1
    return count


# count frequency in sorted array with duplicates - using dict aka map
def countFreqArrayMapApproach(arr, target):
    freq = {}
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    return freq[target]


# find the first occurence of element
def findFirst(arr, target):
    n = len(arr)
    start, end = 0, n - 1

    first = -1
    while start <= end:
        mid = (start + end) // 2

        # if mid matches target
        if arr[mid] == target:
            # mid can be answer
            first = mid
            # but, check the left half also
            end = mid - 1
        elif arr[mid] < target:
            # go to right half
            start = mid + 1
        else:
            # go to left half
            end = mid - 1
    return first


# find the last occurence of target
def findLast(arr, target):
    n = len(arr)
    start, end = 0, n - 1
    last = -1
    while start <= end:
        mid = (start + end) // 2

        # if mid matches target
        if arr[mid] == target:
            # mid can be answer
            last = mid
            # but, check the right half also
            start = mid + 1
        elif arr[mid] < target:
            # search in right half
            start = mid + 1
        else:
            # search in left half
            end = mid - 1
    return last


# find the number of occurences of target in sorted array with duplicates optimal approach
def countFreqArrayOptimal(arr, target):
    first = findFirst(arr, target)
    last = findLast(arr, target)
    if first == -1:
        return 0
    return last - first + 1


# Search Element in Rotated Sorted Array II - return True if present else False
def searchSortedArrayTwoBrute(arr, target):

    for ele in arr:
        if ele == target:
            return True
    return False


def searchSortedArrayTwoOptimal(nums, target):
    n = len(nums)

    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        # if element is present, return True
        if nums[mid] == target:
            return True

        # if start,mid and end points to same number
        if nums[start] == nums[mid] == nums[end]:
            # reduce the search space
            start += 1
            end -= 1
            continue

        # find the sorted half first
        # left sorted
        elif nums[start] <= nums[mid]:
            # check for element in left half
            if nums[start] <= target <= nums[mid]:
                # eliminate the right half
                end = mid - 1
            else:
                # eliminate the left half
                start = mid + 1

        # right sorted
        else:
            # check for element in right half
            if nums[mid] <= target <= nums[end]:
                # eliminate the left half
                start = mid + 1
            else:
                # eliminate the right half
                end = mid - 1

    # element not present
    return False


# Minimum in Rotated Sorted Array -- brute force
def findMinBrute(arr):
    minele = float("inf")
    for ele in arr:
        if ele < minele:
            minele = ele
    return minele


# Minimum in a rotated sorted array -- optimal
def findMinOptimal(arr):
    minele = float("inf")

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        # find sorted half first
        # left sorted
        if arr[start] <= arr[mid]:
            # update minele
            minele = min(arr[start], minele)
            # move on to right part
            start = mid + 1

        # right sorted
        else:
            # update minele
            minele = min(arr[mid], minele)
            # move on to left part
            end = mid - 1

    return minele


# how many times array is rotated - brute force
def timesArrayRotatedBrute(arr):
    n = len(arr)
    minele = min(arr)

    for i in range(n):
        if arr[i] == minele:
            return i


# how many times array is rotated - optimal
def timesArrayRotatedOptimal(arr):
    n = len(arr)
    start, end = 0, n - 1
    minele = float("inf")
    minidx = -1
    while start <= end:
        mid = (start + end) // 2

        # find the sorted half
        # left sorted
        if arr[start] <= arr[mid]:
            # update min element
            if arr[start] < minele:
                minele = arr[mid]
                minidx = start
            # eliminate the left half
            start = mid + 1

        # right sorted
        else:
            # update the min element
            if arr[mid] < minele:
                minele = arr[mid]
                minidx = mid
            # eliminate the right half
            end = mid - 1
    return minidx


# find the single number in a sorted array -- brute force
# every number appears twice except once
def findSingleNumberBrute(arr):
    n = len(arr)
    # only 1 element, return that
    if n == 1:
        return arr[0]
    i = n - 1
    # traverse from the end
    while i >= 0:
        # if current and prev are not equal, then current appears only once
        if arr[i] != arr[i - 1]:
            return arr[i]
        # move to next unique
        i -= 2
    # if you are at first element, then that appears only once
    return arr[i]


# find the single number in a sorted array -- better solution
def findSingleNumberBetter(arr):
    freq = {}
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    for key in freq.keys():
        if freq[key] == 1:
            return key


# find the single number in a sorted array -- xor solution
def findSingleNumberXorSolution(arr):
    ans = 0
    for ele in arr:
        ans ^= ele
    return ans


# find the single number in a sorted array -- optimal solution
def findSingleNumberOptimal(arr):
    n = len(arr)
    # single element, return it
    if n == 1:
        return arr[0]

    # first element is unique
    if arr[0] != arr[1]:
        return arr[0]
    # last element is unique
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    # now , check for index 1 to n-2
    start, end = 1, n - 2

    while start <= end:
        mid = (start + end) // 2

        # check if mid is unique
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        # check if we are in left half
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (
            mid % 2 != 0 and arr[mid] == arr[mid - 1]
        ):
            # go to right half as answer lies in right half
            start = mid + 1

        # you are in right half
        else:
            # to to lefft half as answer lies there
            end = mid - 1


# find peak element in array - brute force
# peak element -- arr[i-1]<arr[i] and arr[i+1]<arr[i]
def findPeakBrute(arr):
    n = len(arr)

    if n == 1:
        return 0

    for i in range(n):
        if i == 0:
            if float("-inf") < arr[i] and arr[i + 1] < arr[i]:
                return i
        elif i == n - 1:
            if float("-inf") < arr[i] and arr[i - 1] < arr[i]:
                return i
        elif arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
            return i


# find peak element in array - optimal
def findPeakOptimal(arr):
    n = len(arr)

    # if array has only 1 element
    if n == 1:
        return 0
    # first element can be peak
    if arr[0] > arr[1]:
        return 0
    # last element can be peak
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # check for the rest elements
    start, end = 1, n - 2

    while start <= end:
        mid = (start + end) // 2

        # if mid is the peak
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        # we are in increasing curve, go to right
        elif arr[mid] > arr[mid - 1]:
            start = mid + 1
        # we are in decreasing curve , go to left
        elif arr[mid] > arr[mid + 1]:
            end = mid - 1
        else:
            # more then 2 peaks are there
            # either go to left or right
            end = mid - 1


def main():
    sys.stdin = open("binary search/input.txt", "r")
    sys.stdout = open("binary search/output.txt", "w")
    input = sys.stdin.readline

    # start here
    arr1 = list(map(int, input().split(",")))
    # target = int(input())
    print(findPeakOptimal(arr1))


threading.Thread(target=main).start()
