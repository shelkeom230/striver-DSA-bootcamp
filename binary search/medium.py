import sys, threading


# find square root of n -- brute force
def findSquareRootBrute(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return i
        i += 1
    return i - 1


import math as m


# find square root of n -- optimal approach 1
def findSquareRootOptimal1(n):
    # use inbuilt sqrt method
    return int(m.sqrt(n))


# find square root of n -- optimal approach 2
def findSquareRootOptimal2(n):

    start, end = 1, n

    while start <= end:
        # calculate middle number
        mid = (start + end) // 2

        # square of mid is less than or equal to n
        if mid * mid <= n:
            # this mid can be the answer,but we need some greater number
            # so , go towards right
            start = mid + 1
        # square of mid exceeds n
        else:
            # go to left and search smaller number
            end = mid - 1
    return end


# find nth root of number M  -- brute force
def findNthRootBrute(n, m):
    for i in range(1, m + 1):
        if i**n == m:
            return i
        if i**n > m:
            break
    return -1


# find nth root of number M  -- optimal
def findNthRootOptimal(n, m):
    # if n is factor of m , don't check further
    if m % n == 0:
        return n

    start, end = 1, m

    while start <= end:
        mid = (start + end) // 2

        if mid**n == m:
            return mid
        elif mid**n > m:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# koko eating bananas -- brute force
def findHrs(arr, hourly):
    totalHrs = 0
    for banana in arr:
        totalHrs += (banana + hourly - 1) // hourly

    return totalHrs


def kokoEatingBananasBrute(n, arr, h):
    maxele = max(arr)

    # find total hours it takes for each k value
    # if for any k it is less than h, then it is our answer
    for k in range(1, maxele + 1):
        totalhrs = findHrs(arr, k)
        if totalhrs <= h:
            return k


# koko eating bananas -- optimal
def kokoEatingBananasOptimal(n, arr, h):
    maxele = max(arr)

    # take 2 pointers
    start, end = 1, maxele

    while start <= end:
        # find mid k value
        mid = (start + end) // 2

        # find total hrs required with current k value
        totalhrs = findHrs(arr, mid)

        # if totalhrs is less than or equal to k , this can be answer
        # but, we need to check for minimum values at left as well
        if totalhrs <= h:
            # go to left
            end = mid - 1
        else:
            # totalhrs exceeds h , so we need to maximise k so that totalhrs reduces , go to right
            start = mid + 1
    # at beginning, start holds answer not possible and end holds possible answer, at the end of loop, opposite polarity will happen , and hence, start is our answer
    return start


# minimum days to make m bouquets -- brute force
def possible(arr, day, m, k):
    n = len(arr)
    if n < m * k:
        return False

    cnt = 0
    noOfBk = 0
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfBk += cnt // k
            cnt = 0

    noOfBk += cnt // k
    return noOfBk >= m


def minBktsBrute(arr, m, k):

    mini, maxi = min(arr), max(arr)

    for i in range(mini, maxi + 1):
        if possible(arr, i, m, k):

            return i
    return -1


# minimum days to make m bouquets -- optimal


def minDays(bloomDay, m, k):

    n = len(bloomDay)

    # if total flowers exceeds array size
    if m * k > n:
        return -1

    # take 2 pointers
    start, end = min(bloomDay), max(bloomDay)

    while start <= end:
        # calculate middle day
        mid = (start + end) // 2

        # find if it is possible to make m with current day
        ans = possible(bloomDay, mid, m, k)
        if ans:
            # if yes, then this mid can be answer
            # but, we need to check for some lower day values , so go to left
            end = mid - 1
        else:
            # this mid, is very smaller, go to right for bigger ones
            start = mid + 1

    # at last, start points to min day due to opposite polarity
    return start


# Find the Smallest Divisor Given a Threshold -- brute force
def findSum(arr, divisor):
    sum = 0
    for i in range(len(arr)):
        sum += (arr[i] + divisor - 1) // divisor

    return sum


def findSmallestDivisor(arr, thresh):
    n = len(arr)

    mini, maxi = float("inf"), float("-inf")

    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    for i in range(mini, maxi + 1):
        divisorSum = findSum(arr, i)
        if divisorSum <= thresh:
            return i


# find the smallest divisor less than or equal to limit -- optimal
def smallestDivisor(arr, limit):
    # Write your code here.

    # pass
    n = len(arr)
    maxi = float("-inf")

    for i in range(n):
        maxi = max(maxi, arr[i])

    start, end = 1, maxi

    while start <= end:
        mid = (start + end) // 2

        currentSum = findSum(arr, mid)

        if currentSum <= limit:
            end = mid - 1
        else:
            start = mid + 1
    return start


# capacity to ship packages with D days
def findDays(weights, cap):
    days, load = 1, 0

    for i in range(len(weights)):
        if load + weights[i] > cap:
            days += 1
            load = weights[i]
        else:
            load += weights[i]
    return days


def bruteSolution(weights, d):
    # min capacity value
    minCapacity = min(weights)
    # max capacity value, d=1
    maxCapacity = sum(weights)

    # check for all possible capacity values
    for i in range(minCapacity, maxCapacity):
        # find no of days required with current capacity
        noofdays = findDays(weights, i)

        # if no of days are less than or equal to d, then this is our answer
        if noofdays <= d:
            return i

    # else just reutrn the max maxCapacity
    return maxCapacity


# capacity to ship packages with D days -- optimal
def leastWeightCapacity(weights, d):
    # Write your code here.
    # pass
    minCapacity = max(weights)
    maxCapacity = sum(weights)

    if d == 1:
        return maxCapacity

    start, end = minCapacity, maxCapacity

    while start <= end:
        mid = (start + end) // 2

        noofdays = findDays(weights, mid)

        if noofdays > d:
            start = mid + 1
        else:
            end = mid - 1

    return start


# kth missing positive number -- brute force
def kthMissingPositiveBrute(arr, k):
    n = len(arr)

    for i in range(n):
        if arr[i] <= k:
            k += 1
        else:
            break
    return k


# kth missing positive number -- optimal
def kthMissingPositiveOptimal(arr, k):
    n = len(arr)

    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        missing = arr[mid] - (mid + 1)

        if missing < k:
            start = mid + 1
        else:
            end = mid - 1
    return end + k + 1


# aggressive cows -- brute force
def isPossible(stalls, dist, k):
    cntCows = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            cntCows += 1
            last = stalls[i]
        if cntCows >= k:
            return True
    return False


def aggCowsBrute(stalls, n, k):
    n = len(stalls)
    stalls.sort()
    minDist, maxDist = 1, stalls[n - 1] - stalls[0]

    for i in range(minDist, maxDist + 1):

        possible = isPossible(stalls, i, k)

        if not possible:
            return i - 1

    return maxDist


# aggressive cows -- optimal
def aggressiveCowsOptimal(stalls, k):
    # Write your code here.
    # pass
    n = len(stalls)
    stalls.sort()
    minDist = 1
    maxDist = stalls[n - 1] - stalls[0]

    start, end = minDist, maxDist

    while start <= end:
        mid = (start + end) // 2

        possible = isPossible(stalls, mid, k)

        if possible == True:
            start = mid + 1
        else:
            end = mid - 1
    return end


# allocate minimum no of pages -- brute force
def countPages(arr, pages):
    students, studentPages = 1, 0

    for i in range(len(arr)):
        if studentPages + arr[i] <= pages:
            studentPages += arr[i]
        else:
            students += 1
            studentPages = arr[i]
    return students


def allocatePagesBrute(arr, m):
    if m > len(arr):
        return -1
    minPages = max(arr)
    maxPages = sum(arr)

    for i in range(minPages, maxPages + 1):

        pages = countPages(arr, i)

        if pages == m:
            return i
    return minPages


# allocate minimum no of pages -- optimal
def allocatePagesOptimal(arr, m):
    if m > len(arr):
        return -1

    start, end = max(arr), sum(arr)

    while start <= end:
        mid = (start + end) // 2

        pages = countPages(arr, mid)

        if pages <= m:
            end = mid - 1
        else:
            start = mid + 1
    return start


# split array largest sum -- brute force
def countPartitions(arr, maxSum):
    part = 1
    subarraySum = 0

    for i in range(len(arr)):
        if arr[i] + subarraySum <= maxSum:
            subarraySum += arr[i]
        else:
            part += 1
            subarraySum = arr[i]

    return part


def splitArrayBrute(arr, k):
    minSum, maxSum = max(arr), sum(arr)
    if len(arr) == k:
        return minSum

    for i in range(minSum, maxSum + 1):
        part = countPartitions(arr, i)

        if part == k:
            return i
    return minSum


# split array largest sum -- optimal
def splitArrayOptimal(arr, k):
    start, end = max(arr), sum(arr)

    while start <= end:
        mid = (start + end) // 2

        part = countPartitions(arr, mid)

        if part == k:
            end = mid - 1
        elif part < k:
            end = mid - 1
        else:
            start = mid + 1
    return start


# painters partition -- brute force
def countPainters(arr, time):
    painters, boardsPainter = 1, 0

    for i in range(len(arr)):
        if arr[i] + boardsPainter <= time:
            boardsPainter += arr[i]
        else:
            painters += 1
            boardsPainter = arr[i]
    return painters


def paintersPartBrute(arr, k):
    minTime, maxTime = max(arr), sum(arr)

    if len(arr) == k:
        return minTime

    for i in range(minTime, maxTime + 1):
        painters = countPainters(arr, i)

        if painters == k:
            return i
    return minTime


# painters pattern -- optimal solution
def paintersPartOptimal(arr, k):
    start, end = max(arr), sum(arr)

    while start <= end:
        mid = (start + end) // 2

        painters = countPainters(arr, mid)

        if painters <= k:
            end = mid - 1
        else:
            start = mid + 1
    return start


# Minimise Maximum Distance between Gas Stations -- brute force
def gasStationBrute(arr, k):
    n = len(arr)

    howManySt = [0] * (n - 1)
    for i in range(1, k + 1):
        maxValue, maxIndex = -1, -1

        for j in range(n - 1):
            diff = arr[j + 1] - arr[j]

            secLength = diff / (howManySt[j] + 1)
            if secLength > maxValue:
                maxValue = secLength
                maxIndex = j

        howManySt[maxIndex] += 1

    # find the ans
    maxAns = -1

    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        secLength = diff / (howManySt[i] + 1)
        maxAns = max(maxAns, secLength)
    return maxAns


import heapq

# gas station -- better solution
# using priority queue


def gas_station_better(arr, k):
    n = len(arr)
    how_many = [0] * (n - 1)

    # max heap: use negative value since Python has min-heap by default
    pq = []
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        heapq.heappush(pq, (-diff, i))

    for _ in range(k):
        # get segment with largest section
        neg_len, i = heapq.heappop(pq)
        how_many[i] += 1

        # recalculate new section length
        diff = arr[i + 1] - arr[i]
        new_len = diff / (how_many[i] + 1)

        # push updated value back into heap
        heapq.heappush(pq, (-new_len, i))

    # return the max section length after placing all k stations
    return -pq[0][0]


# gas station -- optimal solution
def noOfStationsRequired(dist, arr):
    n = len(arr)
    cnt = 0

    for i in range(1, n):
        noInBetween = (arr[i] - arr[i - 1]) // dist
        if (arr[i] - arr[i - 1]) == (dist * noInBetween):
            noInBetween -= 1
        cnt += noInBetween

    return cnt


def gasStationOptimal(arr, k):
    n = len(arr)
    start, end = 0, 0

    # find end value
    for i in range(n - 1):
        end = max(end, arr[i + 1] - arr[i])

    diff = 1e-6
    while end - start > diff:
        mid = (start + end) / 2.0

        noOfStations = noOfStationsRequired(mid, arr)

        if noOfStations > k:
            start = mid
        else:
            end = mid
    return end


def main():
    sys.stdin = open("binary search/input.txt", "r")
    sys.stdout = open("binary search/output.txt", "w")
    input = sys.stdin.readline

    # start here
    # n = int(input())
    arr = list(map(int, input().split(",")))
    m = int(input())
    # k = int(input())
    print(gasStationOptimal(arr, m))


threading.Thread(target=main).start()
