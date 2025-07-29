# medium problems for striver aka
import sys, threading
from itertools import permutations
from collections import defaultdict


# 2 sum, brute force
def twosum_brute(arr, target):
    n = len(arr)

    for i in range(n):
        ele = arr[i]

        for j in range(i + 1, n):
            if arr[j] == target - ele:
                return [i, j]
    return -1


# slight better with hashmap,0*NlogN
def twosum_better(arr, target):
    n = len(arr)
    hash = {}

    for i in range(n):
        ele = arr[i]
        moreRequired = target - ele

        if moreRequired in hash:
            return "YES"
        hash[ele] = i
    return "NO"


# 2sum return the indexes
def twosum_better2(arr, target):
    n = len(arr)
    hash = {}

    for i in range(n):
        element = arr[i]
        moreRequired = target - element

        if moreRequired in hash:
            return [hash[moreRequired], i]
        hash[element] = i
    return -1


# most optimal approach , 0(N)+0(NlogN)=0(N), 2 ptrs, it can't return indexes, just returns true or false


def twosum_optinal(arr, target):
    n = len(arr)
    left, right = 0, n - 1
    arr = sorted(arr)

    while left < right:
        if arr[left] + arr[right] == target:
            return "YES"
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return "NO"


# sort an array of 0 , 1 and 2, 0(nlogn)
def sort_array_brute(arr):
    return sorted(arr)


# slight better approach, with counters 0(N)
def sort_array_better(arr):
    cnt0, cnt1, cnt2 = 0, 0, 0

    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 1:
            cnt1 += 1
        elif arr[i] == 2:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0
    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1
    for i in range(cnt0 + cnt1, n):
        arr[i] = 2
    return arr


# most optimal approach , dutch national flag algorithm
def sort_array_optimal(arr):
    n = len(arr)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# majority element in an array, brute force 0(n^2)
def majority_element_brute(arr):
    n = len(arr)

    for i in range(n):
        cnt = 0
        ele = arr[i]
        for j in range(n):
            cnt += 1 if arr[j] == ele else 0

        if cnt > (n // 2):
            return ele
    return -1


# majority element in array (occurs N//2 times ), better approach 0(NlogN)
def majority_element1(arr):
    n = len(arr)
    hash = {}

    for ele in arr:
        hash[ele] = hash.get(ele, 0) + 1

    for key, val in hash.items():
        if val > (n // 2):
            return key
    return -1


# most optimal, moore's majority voting algorithm
def majority_element_optimal(arr):
    n = len(arr)

    cnt0, cnt1, ele = 0, 0, 0

    for i in range(n):
        if cnt0 == 0:
            cnt0 = 1
            ele = arr[i]
        elif arr[i] == ele:
            cnt0 += 1
        else:
            cnt0 -= 1

    for i in range(n):
        cnt1 += 1 if arr[i] == ele else 0

    if cnt1 > (n // 2):
        return ele
    else:
        return -1


# max subarray sum , most brute force approach 0(N^3)
def maxSubArraySum_brute(arr):
    maxSum = float("-inf")

    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += arr[k]
            maxSum = max(maxSum, sum)
    return maxSum


# max subarray sum, quite better approach, 0(N^2) , eliminate last kth loop
def maxSubarraySum_better(arr):
    maxSum = float("-inf")

    n = len(arr)
    if n == 1:
        return arr
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            maxSum = max(maxSum, sum)
    return maxSum


# most optimal approach, kadane's algo , 0(N)
def maxSubarraySum_optimal(arr):
    maxSum = float("-inf")
    n = len(arr)
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxSum:
            maxSum = sum

        if sum < 0:
            sum = 0
    return maxSum


# follow up question, return the indexes of the subarray with given max sum
def maxSubarraySum_indexes(arr):
    sum, maxSum, start, ansStart, ansEnd = 0, float("-inf"), 0, 0, 0

    n = len(arr)

    for i in range(n):
        if sum == 0:
            start = i

        sum += arr[i]

        if sum > maxSum:
            maxSum = sum
            ansStart = start
            ansEnd = i

        if sum < 0:
            sum = 0

    print(f"[", end=" ")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=", ")
    print("]")

    if maxSum < 0:
        maxSum = 0
    return maxSum


# stock buy and sell, brute force, 0(N^2)
def stockBuySell_brute(arr):
    n = len(arr)
    maxProfit = float("-inf")

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                maxProfit = max(maxProfit, arr[j] - arr[i])
    if maxProfit < 0:
        maxProfit = 0
    return maxProfit


# stock buy and sell, most optimal, 2ptrs ,0(N)
def stockBuySell_optimal(arr):
    maxProfit = float("-inf")
    minPrice = arr[0]

    n = len(arr)

    for i in range(1, n):
        cost = arr[i] - minPrice
        maxProfit = max(maxProfit, cost)
        minPrice = min(minPrice, arr[i])
    return maxProfit


# arrange elements in array with alternate sign (equal +ve and -ve), brute force,0(N), 0(N) both
def alternateSign_brute(arr):
    n = len(arr)

    pos, neg = [], []

    for ele in arr:
        neg.append(ele) if ele < 0 else pos.append(ele)

    for i in range(n // 2):
        arr[2 * i] = pos[i]
        arr[2 * i + 1] = neg[i]
    return arr


# arrange elements in array with alternate sign (equal +ve and -ve), optimal,0(N), 0(1)
def alternateSign_optimal(arr):
    n = len(arr)
    posIndex, negIndex = 0, 1
    ans = [0] * n

    for i in range(n):
        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex += 2
        else:
            ans[posIndex] = arr[i]
            posIndex += 2
    return ans


# follow up questions, # of +ve and -ve elements are not equal,
def alternateSign_followup(arr):
    n = len(arr)

    pos, neg = [], []

    for ele in arr:
        neg.append(ele) if ele < 0 else pos.append(ele)

    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]

        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1
    return arr


# generate next greater permutation
def nextPermutation_brute(arr):
    if arr == sorted(arr, reverse=True):
        return sorted(arr)

    perm = list(permutations(arr))

    perm = [list(p) for p in perm]

    for i in range(len(perm)):
        if perm[i] == arr:
            return perm[i + 1]


# next greater permutation , optimal appraoch
def nextPermutation_optimal(arr):
    n = len(arr)
    index = -1

    # find the break point
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            index = i
            break

    # if index==-1, just return the sroted array
    if index == -1:
        arr.reverse()
        return arr

    # find first element greater than index
    for i in range(n - 1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break

    # sort the remaining array
    arr[index + 1 :] = sorted(arr[index + 1 :])
    return arr


# Leaders in an array , a leader is an element which is greter than all elements to it's right
# 0(N^2), 0(N)
def findLeaders_brute(arr):
    n = len(arr)
    leaders = []

    for i in range(n):
        isLeader = True
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                isLeader = False
                break

        if isLeader:
            leaders.append(arr[i])
    return leaders


# Leaders in an array, most optimal approach, 0(N), 0(N) worst
def findLeaders_optimal(arr):
    leaders = []

    n = len(arr)
    maxi = float("-inf")

    for i in range(n - 1, -1, -1):
        if arr[i] > maxi:
            leaders.append(arr[i])
            maxi = arr[i]
    leaders.reverse()
    return leaders


# find the longest consecutive subsequence from the array
def longestConsecutive_Sequence_brute(arr):
    n = len(arr)
    longest = 1

    if n == 0:
        return 0

    for i in range(n):
        cnt = 1
        ele = arr[i] + 1
        while ele in arr:
            cnt += 1
            ele += 1
        longest = max(longest, cnt)
    return longest


# longest consecutive sequence , better, 0(NlogN), 0(1)
def longestConsecutive_better(arr):
    n = len(arr)

    if n == 0:
        return 0
    cntCurr, longest, lastSmaller = 0, 1, float("-inf")
    arr = sorted(arr)

    for i in range(n):
        if arr[i] - 1 == lastSmaller:
            cntCurr += 1
            lastSmaller = arr[i]
        elif arr[i] != lastSmaller:
            cntCurr = 1
            lastSmaller = arr[i]
        longest = max(longest, cntCurr)
    return longest


# longest consecutive sequence, most optimal solution 0(N)
def longestConsecutive_optimal(arr):
    n = len(arr)

    if n == 0:
        return 0

    longest = 1
    cnt = 0
    s = set()
    for ele in arr:
        s.add(ele)

    for ele in s:
        if ele - 1 not in s:
            cnt = 1
            x = ele

            while x + 1 in s:
                cnt += 1
                x += 1
            longest = max(longest, cnt)
    return longest


# set matrix zeros ,brute force solutoin


def markRow(i, mat):
    for j in range(len(mat[i])):
        if mat[i][j] != 0:
            mat[i][j] = -1


def markCol(j, mat):
    for i in range(len(mat)):
        if mat[i][j] != 0:
            mat[i][j] = -1


def setMatrixZeros_brute(mat):
    n = len(mat)
    # marking as -1
    for i in range(n):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                markRow(i, mat)
                markCol(j, mat)

    # change to -1
    for i in range(n):
        for j in range(len(mat[i])):
            if mat[i][j] == -1:
                mat[i][j] = 0
    return mat


# mark matrix as zeros, better solution
def setMatrixZeros_better(mat, n, m):

    rows, cols = [0] * n, [0] * m
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                rows[i], cols[j] = 1, 1

    for i in range(n):
        for j in range(m):
            if rows[i] == 1 or cols[j] == 1:
                mat[i][j] = 0

    return mat


# set matrix zeros, most optimal solution , in space
def setMatrixZeros_optimal(mat, n, m):
    col0 = 1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                # mark the col
                if j != 0:

                    mat[0][j] = 0
                else:
                    col0 = 0

                # mark the row
                mat[i][0] = 0

    # mark for the rest elements except first row and col
    for i in range(1, n):
        for j in range(1, m):
            # check marker for row and col
            if mat[0][j] == 0 or mat[i][0] == 0:
                mat[i][j] = 0

    # set the 1st col first
    if mat[0][0] == 0:
        for i in range(n):
            mat[i][0] = 0

    # set the 1st row
    if col0 == 0:
        for j in range(m):
            mat[i][0] = 0
    return mat


# rotate matrix clockwise by 90 deg, brute force,
def rotateMatrixClk_brute(mat, n, m):
    ans = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            ans[j][n - 1 - i] = mat[i][j]
    return ans


# rotate matrix by 90% clockwise , optimal one, 0(n*m)
def rotateMatrixClk_optimal(matrix, n, m):
    for i in range(n - 1):
        for j in range(i + 1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for row in matrix:
        row.reverse()

    for row in matrix:
        print(row)


# pritn matrix in spiral order, only optimal solution


def printMatrixSpiral_optimal(matrix, n, m):
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    res = []
    while left <= right and top <= bottom:
        # right
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1

        # bottom
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        # left
        if top <= bottom:  # there is any row
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

        # top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


# count subarrays with sum =k , brute force
def countSubarrays_sumK_brute(arr, n, k):
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == k:
                cnt += 1
    return cnt


# count subarrays with sum=k, most optimal, dict and prefix sum approach, 0(N*logN)
def countSubarrays_sumK_optimal(arr, n, k):
    cnt = 0
    mpp = defaultdict(int)
    prefixSum = 0

    mpp[0] = 1
    for i in range(n):
        # add current val to prefixsum
        prefixSum += arr[i]

        # calculate required sum
        remove = prefixSum - k

        # increment counter if remove is found in map
        cnt += mpp[remove]

        # update the cnt of sum in mpp
        mpp[prefixSum] += 1
    return cnt


import math as m


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
def printValueAtIndexes(n):
    ans = 1
    for i in range(r):
        ans = ans * (n - i)
        ans = ans // (i + 1)
    return ans


def main():
    sys.stdin = open("arrays/input.txt", "r")
    sys.stdout = open("arrays/output.txt", "w")
    input = sys.stdin.readline

    # start here3
    n = int(input())
    # arr = list(map(int, input().split()))
    i = 4
    print(printIthRowPascalTriangle(n))


threading.Thread(target=main).start()
