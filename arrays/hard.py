# hard problems here
import sys, threading, math as m
from collections import Counter
from collections import defaultdict


# print the pascal triangle ,brute force
def printPascalTriangle_brute(n, c, r):
    for i in range(n):
        for j in range(0, i + 1):
            print(m.comb(i, j), end=" ")
        print()


# implement the formula
def printPascalTriangle_brute2(n, c, r):
    for i in range(n):
        for j in range(i + 1):
            val = m.factorial(i) / (m.factorial(j) * m.factorial(i - j))
            print(int(val), end=" ")
        print()


# use 2D array for calculation
def printPascalTriangle_brute3(n, c, r):
    ans = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if i == 0 or j == i:
                ans[i][j] = 1
            else:
                ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]

    # print the triangle
    for i in range(len(ans)):
        for j in range(i + 1):
            print(ans[i][j], end=" ")
        print()


# print ith row in pascal triangle
def printIthRowPascalTriangle(n):
    ans = 1
    print(ans, end=" ")
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end=" ")
    print()


# print the value at col c and row r in pascal triangle
def printValueAtIndexes(r, n):
    ans = 1
    for i in range(r):
        ans = ans * (n - i)
        ans = ans // (i + 1)
    return ans


# find value at row r and col c
def ncr(n, r):
    ans = 1

    for i in range(r):
        ans *= n - i
        ans //= i + 1
    return ans


# variation 3 , brute force 0(n^3)
def pascalTriangle(n):
    ans = []

    for row in range(1, n + 1):
        temp = []
        for col in range(1, row + 1):
            temp.append(ncr(row - 1, col - 1))
        ans.append(temp)
    return ans


def generateRow(row):
    ans = 1
    ansRow = [1]

    for col in range(1, row):
        ans *= row - col
        ans //= col
        ansRow.append(ans)
    return ansRow


# most optimal one
def pascalTriangleOptimal(n):
    ans = []

    for row in range(1, n + 1):
        ans.append(generateRow(row))
    return ans


# element occuring more than n/3 times - brute force - 0(N^2), 0(1)
def MoreThanNby3Brute1(arr):
    n = len(arr)
    res = []
    for i in range(n):
        ele = arr[i]
        cnt = 0
        for j in range(n):
            if ele == arr[j]:
                cnt += 1
        if cnt > n // 3 and ele not in res:
            res.append(ele)
        if len(res) == 2:
            return res


# use dict - 0(N)
def MoreThanNBy3Brute2(arr):
    n = len(arr)
    hash = {}
    res = []
    for ele in arr:
        if ele in hash:
            hash[ele] += 1
        else:
            hash[ele] = 1

    for key, val in hash.items():
        if val > n // 3:
            res.append(key)
    return res


# another short approach with dict
def MoreThanNBy3Better(arr):
    n = len(arr)
    counter = Counter(arr)

    for num, count in counter.items():
        if count > n // 2:
            return num
    return -1


# most optimal approach using cancellation approach - 0(N), 0(1)
def MoreThanNBy3Optimal(arr):
    n = len(arr)

    # get all possible answers
    cnt1, cnt2 = 0, 0
    ele1, ele2 = float("-inf"), float("-inf")
    res = []
    for i in range(n):
        if cnt1 == 0 and arr[i] != ele2:
            cnt1 = 1
            ele1 = arr[i]
        elif cnt2 == 0 and arr[i] != ele1:
            cnt2 = 1
            ele2 = arr[i]
        elif arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    # manually check for the answers
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if arr[i] == ele1:
            cnt1 += 1
        if arr[i] == ele2:
            cnt2 += 1

    mini = (n // 3) + 1
    if cnt1 >= mini:
        res.append(ele1)
    if cnt2 >= mini:
        res.append(ele2)
    return res


# 4 sum --> find quads that add upto a target value --> extreme brute force -0(N^4) very bad
def fourSum(arr, target):
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        quad = sorted([arr[i], arr[j], arr[k], arr[l]])
                        st.add(tuple(quad))

    return [list(quad) for quad in st]


# 4 sum better --> using set - 0(N^3)
def fourSumBetter(arr, target):
    n = len(arr)
    st = set()
    arr.sort()

    for i in range(n):
        for j in range(i + 1, n):
            hashset = set()
            for k in range(j + 1, n):
                sum_ = arr[i] + arr[j] + arr[k]
                fourth = target - sum_

                if fourth in hashset:
                    quad = tuple(sorted((arr[i], arr[j], arr[k], fourth)))

                    st.add(quad)
                hashset.add(arr[k])
    return [list(quad) for quad in st]


# most optimal approach, 2 loops and 2 pointers - 0(N^2)
def fourSumOptimal(nums, target):
    n = len(nums)
    ans = set()
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            k, l = j + 1, len(nums) - 1
            while k < l:
                sum_ = nums[i] + nums[j] + nums[k] + nums[l]

                if sum_ == target:
                    quad = tuple((nums[i], nums[j], nums[k], nums[l]))
                    ans.add(quad)
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                elif sum_ < target:
                    k += 1
                else:
                    l -= 1
    return [list(quad) for quad in ans]


# Length of longest subarray with sum 0 - brute force
def LongestSubarraySumZeroBrute(arr):
    n = len(arr)
    maxLength = 0
    for i in range(n):

        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == 0:
                maxLength = max(maxLength, j - i + 1)

    return maxLength


# LongestSubarraySumZero optimal --> prefix sum and hashmap
def LongestSubarraySumZeroOptimal(arr):
    n = len(arr)
    map = {}
    maxLength = 0
    sum = 0
    for i in range(n):
        sum += arr[i]

        if sum == 0:
            maxLength = i + 1
        else:
            if sum in map.keys():
                maxLength = max(maxLength, i - map[sum])
            else:
                map[sum] = i
    return maxLength


# print the subarrays with given xor k - better
def SubarraysWithXorK(arr, k):
    n = len(arr)
    ans = []

    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= arr[j]
            if xor == k:
                ans.append(arr[i : j + 1])
    return ans


# count number of subarrays with xor equal to k - extreme brute force - 0(N^3)
def SubarraysWithXorKBruteForce(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            xor = 0
            for k in range(i, j + 1):
                xor ^= arr[k]
                if xor == k:
                    cnt += 1
    return cnt


# count the number of subarrays with given xor k - 0(N^2)
def SubarraysWithXorKBetter(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= arr[j]
            if xor == k:
                cnt += 1
    return cnt


# count subarrays with given xor k - optimal solution with prefix xor - 0(N)
def SubarraysWithXorKOptimal(arr, b):
    n = len(arr)
    xr = 0
    map = defaultdict(int)
    map[xr] = 1
    cnt = 0

    for i in range(n):
        xr ^= arr[i]

        # x
        x = xr ^ b
        cnt += map[x]
        map[xr] += 1
    return cnt


# merge overlapping subintervals -- 0(NlogN)+0(2*N)
def mergeOverlappingSubIntervalsbrute(arr):
    n = len(arr)
    # ans list
    ans = []

    # sort given intervals
    arr.sort()

    for i in range(n):  # start selecting intervals
        start, end = arr[i][0], arr[i][1]

        if ans and end <= ans[-1][1]:
            continue

        # check for next intervals
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans


# merge overlapping subintervals -- optimal solution 0(N)
def mergeOverlappingSubIntervalsOptimal(arr):
    n = len(arr)

    ans = []

    # sort given intervals
    arr.sort()

    for i in range(n):
        # if the current interval cannot be the part of last interval
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current inteval can be the part of last interval
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans


# merge 2 sorted arrays without extra space -- brute force -0(N), 0(N+M)
def mergeTwoSortedArraysBrute(arr1, arr2, n, m):
    left, right = 0, 0
    index = 0
    arr3 = [0] * (n + m)

    # append the smaller element
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1

    # append the remaining elements
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1

    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1

    # copy back to arr1 and arr2
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]

    return arr1, arr2


# optimal solution 1 -- using 2 pointer approach
def mergeTwoSortedArraysOptimal1(arr1, arr2, m, n):
    left, right = m - 1, 0

    while left >= 0 and right < n:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break


def mergeTwoSortedArraysOptimal2(arr1, arr2, n, m):
    def swapIfGreater(arr1, arr2, idx1, idx2):
        if arr1[idx1] > arr2[idx2]:
            arr1[idx1], arr2[idx2] = arr2[idx2], arr1[idx1]

    length = n + m
    gap = (length // 2) + (length % 2)

    while gap > 0:
        left = 0
        right = left + gap

        while right < length:
            # Case 1: left in arr1, right in arr2
            if left < n and right >= n:
                if right - n < m:  # Ensure right is within arr2's bounds
                    swapIfGreater(arr1, arr2, left, right - n)
            # Case 2: left and right in arr2
            elif left >= n:
                if left - n < m and right - n < m:  # Ensure both are within arr2
                    swapIfGreater(arr2, arr2, left - n, right - n)
            # Case 3: left and right in arr1
            else:
                if right < n:  # Ensure right is within arr1
                    swapIfGreater(arr1, arr1, left, right)

            left += 1
            right += 1

        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)

    return arr1, arr2


# find the repeating and missing numbers in an array - brute force 1 - 0(N^2)
def findRepeatingAndMissingBrute(arr, n):
    repeating, missing = -1, -1

    for i in range(1, n + 1):
        cnt = 0

        for j in range(n):
            if arr[j] == i:
                cnt += 1

        if cnt == 2:
            repeating = i
        elif cnt == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break

    return [repeating, missing] if repeating != -1 and missing != -1 else [-1, -1]


# find the repeating and missing numbers in an array - better 1
def findRepeatingAndMissingBetter(arr, n):

    # store freq of each element
    hash = {}
    for ele in arr:
        if ele in hash:
            hash[ele] += 1
        else:
            hash[ele] = 1

    # find ele with freq 2
    for key, val in hash.items():
        if val == 2:
            A = key
            break

    arr.remove(A)
    totalSum = n * (n + 1) // 2
    currentSum = 0
    for ele in arr:
        currentSum += ele
    B = totalSum - currentSum
    return A, B


# striver aka approach - hash array - 0(N)
def findRepeatingAndMissingAka(arr, n):
    hash = [0] * (n + 1)

    for i in range(n):
        hash[arr[i]] += 1

    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        if hash[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break

    return [repeating, missing] if repeating != -1 and missing != -1 else [-1, -1]


# better solution --> use only dict
def findRepeatingAndMissingBetter(arr, n):
    hash = {}
    for ele in arr:
        hash[ele] = hash.get(ele, 0) + 1

    for i in range(1, n + 1):
        if hash.get(i, 0) == 2:
            A = i
        if i not in hash:
            B = i
    return [A, B]


# Optimal solution 1 -- using Maths linear eqn with 2 variables
def findRepeatingAndMissingNumberOptimal1(arr, n):
    sn = (n * (n + 1)) // 2
    s2n = (n * (n + 1) * (2 * n + 1)) // 6
    s, s2 = 0, 0
    for ele in arr:
        s += ele
        s2 += ele * ele

    val1 = s - sn
    val2 = s2 - s2n
    val2 = val2 // val1

    x = (val1 + val2) // 2
    y = val2 - x
    return [x, y]


# count inversions in an array - brute force
def countInversionsBruteForce(arr, n):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i < j and arr[j] < arr[i]:
                cnt += 1
    return cnt


# merge function
def merge(arr, low, mid, high):
    left, right = low, mid + 1
    tmp = []
    cnt = 0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            cnt += mid - left + 1
            right += 1

    while left <= mid:
        tmp.append(arr[left])
        left += 1

    while right <= high:
        tmp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = tmp[i - low]
    return cnt


# merge sort
def merge_sort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt

    mid = (low + high) // 2

    cnt += merge_sort(arr, low, mid)
    cnt += merge_sort(arr, mid + 1, high)
    cnt += countInversions(arr, low, mid, high)
    merge(arr, low, mid, high)
    return cnt


# count inversions optimal approach using merge sort -- 0(NlogN)
def countInversionsOptimal(arr, n):
    return merge_sort(arr, 0, n - 1)


# Count Reverse Pairs -- brute force - 0(N^2)
def countRevPairsBrute(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j] * 2:
                cnt += 1
    return cnt


def countInversions(arr, low, mid, high):
    cnt = 0
    right = mid + 1
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += right - (mid + 1)
    return cnt


# count reverse pairs -- optimal using merge sort
def countReversePairsOptimal(arr):
    n = len(arr)
    return merge_sort(arr, 0, n - 1)


# Maximum Product Subarray in an Array - brute -0(N^3)
def maxProductSubarrayBrute(arr):
    n = len(arr)
    maxP = float("-inf")
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= arr[k]
            maxP = max(maxP, product)
    return maxP


# Maximum Product Subarray in an Array - better - 0(N^2)
def maxProductSubarrayBetter(arr):
    n = len(arr)
    maxProduct = float("-inf")
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            maxProduct = max(maxProduct, product)
    return maxProduct


# Maximum Product Subarray in an Array - optimal - 0(N)
def maxProductSubarrayOptimal(arr):
    n = len(arr)
    maxP = float("-inf")
    preProd, suffixProd = 1, 1
    for i in range(n):
        if preProd == 0:
            preProd = 1
        if suffixProd == 0:
            suffixProd = 1

        preProd *= arr[i]
        suffixProd *= arr[n - i - 1]
        maxP = max(maxP, max(preProd, suffixProd))
    return maxP


def main():

    sys.stdin = open("arrays/input.txt", "r")
    sys.stdout = open("arrays/output.txt", "w")
    input = sys.stdin.readline

    # start here3
    # n = int(input())
    arr1 = list(map(int, input().split(",")))
    print(maxProductSubarrayOptimal(arr1))


threading.Thread(target=main).start()
