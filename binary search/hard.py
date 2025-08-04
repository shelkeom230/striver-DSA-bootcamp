# binary search on grids
import sys, threading


# row with max number of ones -- brute force
def rowWithMax1Brute(mat):
    n = len(mat)
    m = len(mat[0])

    maxIndx = -1
    maxCount = 0
    for i in range(n):
        cnt = sum(mat[i])
        if cnt > maxCount:
            maxCount = cnt
            maxIndx = i

    return maxIndx


# row with max 1 optimal
def lowerBound(arr, x):
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


def rowWithMax1Optimal(mat):
    n = len(mat)

    maxCount = 0
    minIdx = -1
    for i in range(n):
        cnt_ones = lowerBound(mat[i], 1)

        if cnt_ones > maxCount:
            maxCount = cnt_ones
            minIdx = i
    return minIdx


# search in a sorted 2D matrix -- brute
def searchElementBrute(matrix, target):
    # Write your code here.
    # pass
    n = len(matrix)
    m = len(matrix[0])

    isFound = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                isFound = 1

        if isFound == 1:
            break

    return isFound


# search in a sorted 2D matrix -- better
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


def searchMatrixBetter(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        coli = binarySearchIterative(matrix[i], target)
        if coli != -1:
            return [i, coli]
    return [-1, -1]


# binary search -- optimal
def searchMatrixOptimal(mat, target):
    n = len(mat)
    m = len(mat[0])

    total = n + m
    start, end = 0, total - 1

    while start <= end:
        mid = (start + end) // 2

        rowi = mid // m
        coli = mid % m

        if mat[rowi][coli] == target:
            return True
        elif mat[rowi][coli] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


# search in a row-wise and column wise sorted matrix -- brute force
def searchMatrix2Brute(matrix, x):
    # Write your code here.
    # pass
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == x:
                return [i, j]

    return [-1, -1]


# search in a row-wise and column wise sorted matrix -- better
def searchMatrix2Better(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    coli = -1
    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            coli = binarySearchIterative(matrix[i], target)
            if coli != -1:
                return [i, coli]
    return [-1, -1]


# search in a row-wise and column wise sorted matrix -- optimal
def searchMatrix3Optimal(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    i, j = 0, m - 1

    while i < n and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1

    return [-1, -1]


# find peak element in a 2D matrix -- brute force
def findPeak2DBrute(mat):
    n = len(mat)
    m = len(mat[0])

    maxElement = float("-inf")
    for i in range(n):
        for j in range(m):
            maxElement = max(maxElement, mat[i][j])

    return maxElement


# find peak element in a 2D matrix -- optimal
def maxElement(mat, n, m, col):
    maxEle = -1
    rowIndx = -1
    for i in range(n):
        if mat[i][col] > maxEle:
            maxEle = mat[i][col]
            rowIndx = i
    return rowIndx


def findPeak2DOptimal(mat):
    n = len(mat)
    m = len(mat[0])

    start, end = 0, m - 1

    while start <= end:
        mid = (start + end) // 2
        row = maxElement(mat, n, m, mid)

        left = mat[row][mid - 1] if mid - 1 >= 0 else -1
        right = mat[row][mid + 1] if mid + 1 < m else -1

        if mat[row][mid] > left and mat[row][mid] > right:
            return [row, mid]
        elif mat[row][mid] < left:
            end = mid - 1
        else:
            start = mid + 1
    return [-1, -1]


# median of a row wise sorted matrix -- brute force
def medianMatrixBrute(mat):
    # flatten to a 1D array, sort the list and return the median
    n = len(mat)
    m = len(mat[0])
    flat = []
    for i in range(n):
        for j in range(m):
            flat.append(mat[i][j])

    flat.sort()
    return flat[(n * m) // 2]


# find median in a sorted matrix -- optimal
def upperBound(arr, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for a smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans


def countSmallEqual(matrix, m, n, x):
    cnt = 0
    for i in range(m):
        cnt += upperBound(matrix[i], x, n)
    return cnt


def medianMatrixOptimal(matrix, m, n):
    low = float("inf")
    high = float("-inf")

    # point low and high to the right elements
    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])

    req = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEqual(matrix, m, n, mid)
        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low


def main():
    sys.stdin = open("binary search/input.txt", "r")
    sys.stdout = open("binary search/output.txt", "w")
    input = sys.stdin.readline

    # start here
    n = int(input())
    # k = int(input())
    mat = [list(map(int, input().split(","))) for _ in range(n)]
    # arr2 = list(map(int, input().split(",")))
    # m = int(input())
    print(medianMatrixBrute(mat))


threading.Thread(target=main).start()
