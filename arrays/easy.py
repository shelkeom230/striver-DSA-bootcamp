import sys
import threading


def find_largest_brute(arr):
    # brute force solution

    arr = sorted(arr)
    return arr[len(arr) - 1]


def find_largest(arr, n):
    # 0(n) solution

    max = arr[0]
    for ele in arr:
        if ele > max:
            max = ele
    return max


def rec_find_largest(arr, n):
    if n == 1:
        return arr[0]

    # return the max between the last and remaining element
    return max(arr[n - 1], rec_find_largest(arr, n - 1))


# 2 pointer find larget 0(n)
def find_largest_2ptr(arr):
    l, r = 0, len(arr) - 1
    max = float("-inf")
    while l < r:
        if arr[l] > arr[r]:
            max = arr[l]
            r -= 1
        else:
            max = arr[r]
            l += 1
    return max


# find 2nd largest
def find_second_largest1(arr, n):

    maxele = max(arr)
    sl = float("-inf")

    if n < 2:
        return -1
    for ele in arr:
        if ele < maxele and ele > sl:
            sl = ele
    return sl if sl != float("-inf") else -1


def find_second_largest2(arr, n):
    # brute force
    maxele = max(arr)

    for i in range(n - 2, -1, -1):
        if arr[i] != maxele:
            return arr[i]


def find_second_largest3(arr, n):
    # slight better approach
    maxele = arr[0]

    for i in range(1, n):
        if arr[i] > maxele:
            maxele = arr[i]

    sl = -1
    for i in range(n):
        if arr[i] > sl and arr[i] != maxele:
            sl = arr[i]
    return sl


def find_second_smallest(arr, n):
    smallest = arr[0]
    ssmallest = float("+inf")

    for i in range(1, n):
        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]
        elif arr[i] != smallest and arr[i] < ssmallest:
            ssmallest = arr[i]
    return ssmallest


def find_largest_smallest(arr, n):
    slargest = find_second_largest3(arr, n)
    smallest = find_second_smallest(arr, n)
    return slargest, smallest


# check sorted array
def check_sorted(arr, n):
    # brute force approach
    dup = arr
    return sorted(arr) == dup


def check_sorted2(arr, n):
    # another brute force approach 0(n)
    if n == 1:
        return True
    isSorted = True

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            isSorted = False
            return isSorted
    return isSorted


def check_sorted3(arr, n):
    if n == 1:
        return True

    l, r = 0, n - 1
    while l <= r:
        if arr[l] > arr[r]:
            return False
        l += 1
        r -= 1
    return True


# brute force approach
def remove_duplicates1(arr, n):
    st = set()

    for ele in arr:
        if ele not in st:
            st.add(ele)
    return list(st)


# optimised 2 pointer appraoch returns size of unique array
def remove_duplicates2(arr, n):
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1
    return i + 1


# left rotate an array by 1 ,optimal solution
def left_rotate_by1(arr, n):
    first = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[n - 1] = first
    return arr


# Right rotate array by D , brute force
def right_rotate_byd_brute(nums, k):
    n = len(nums)
    k = k % n

    # copy to temp
    temp = nums[n - k :]

    # shifting
    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]

    # copy back temp to nums
    for i in range(k):
        nums[i] = temp[i]
    return nums


# left rotate an array by D places , brute force
def left_rotate_byd(arr, n, d):
    tmp = arr[0:d]

    # shifting
    for i in range(d, n):
        arr[i - d] = arr[i]

    # copy back tmp array at last
    for i in range(n - d, n):
        arr[i] = tmp[i - (n - d)]
    return arr


# Left rotate an array by D places, optimal S.C --> 0(1)
def rev(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate_byd_optimal(arr, d):
    n = len(arr)
    d = d % n
    rev(arr, 0, d - 1)
    rev(arr, d, n - 1)
    rev(arr, 0, n - 1)
    return arr


# move all zeros to the end brute
def move_zeros_brute(arr):
    z = 0
    notzero = []
    for ele in arr:
        if ele == 0:
            z += 1
        else:
            notzero.append(ele)

    for i in range(z):
        notzero.append(0)
    arr = notzero
    return arr


# move all zeros to end striver brute force
def move_all0brute_striver(arr):
    temp = []

    # copy non zero elements to temp
    for ele in arr:
        if ele != 0:
            temp.append(ele)

    # copy back temp to arr
    for i in range(len(temp)):
        arr[i] = temp[i]

    # add zeros at end
    for i in range(len(temp), len(arr)):
        arr[i] = 0
    return arr


# optimal solution, without extra space 2 ptr
def move_0atend_opt(arr):
    j = -1
    # first index of first 0
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break

    for k in range(j + 1, len(arr)):
        if arr[k] != 0:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
    return arr


# linear search
def linear_search(arr, k):
    for i in range(len(arr)):
        if k == arr[i]:
            return i
    return -1


# find common and unique elements from 2 lists
def findCommon(arr1, arr2):
    return sorted(set(arr1) | set(arr2))  # | denotes est union operation


def findCommon_bruteaka(arr1, arr2):
    s = set()
    for ele in arr1:
        if ele not in s:
            s.insert(ele)
    for ele in arr2:
        if ele not in s:
            s.insert(ele)

    return list(set)


def findUnion_optimal(arr1, arr2):
    un = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(un) == 0 or un[-1] != arr1[i]:
                un.append(arr1[i])
            i += 1
        else:
            if len(un) == 0 or un[-1] != arr2[j]:
                un.append(arr2[j])
            j += 1

    # append the remaining elements from arr1 and arr2
    while i < len(arr1):
        if un[-1] != arr1[i]:
            un.append(arr1[i])
        i += 1

    while j < len(arr2):
        if un[-1] != arr2[j]:
            un.append(arr2[j])
        j += 1

    return un


# find missing number in an array
def findMising_optimal1(arr):
    n = len(arr) + 1
    totalSum = n * (n + 1) / 2
    currSum = sum(arr)
    return int(totalSum - currSum)


# quite better solution, find missing number
def find_missing_brute2(arr):
    for i in range(1, len(arr) + 1):
        if i not in arr:
            return i


# better approach using hashing
def find_missing_better(arr):
    n = len(arr)
    freq = [0] * (n + 1)
    for i in range(n - 1):
        freq[arr[i]] += 1

    for i in range(1, n + 1):
        if freq[i] == 0:
            return i


# most optimal solution with xor
def find_missing_optimal(arr):
    n = len(arr) - 1
    xor1, xor2 = 0, 0
    for i in range(n):
        xor2 ^= arr[i]
        xor1 ^= i + 1
    xor1 ^= n + 1
    return xor1 ^ xor2


# maximum consecutive ones in the array
def max_cons_ones(arr):
    cnt = 0
    current = 0
    i = 0

    while i < len(arr):
        if arr[i] == 1:
            current += 1
            cnt = max(cnt, current)
        else:
            current = 0
        i += 1
    return cnt


# check for pythagorean triplet
def istriplet(a, b, c):
    maximum = a

    if b >= a:
        maximum = b
    if c >= a:
        maximum = c

    if maximum == a:
        return a * a == b * b + c * c
    elif maximum == b:
        return b * b == a * a + c * c
    else:
        return c * c == a * a + b * b


# find inverse of an array
def find_inverse(n):
    inv = 0
    op = 1  # original position tracker

    while n != 0:
        od = n % 10  # original digit
        id = op  # inverse digit is current position
        ip = od  # inverse position is the digit's value

        # Set the digit 'id' at position 'ip' in the inverse number
        inv += id * (pow(10, ip - 1))

        op += 1
        n //= 10

    return inv


# check for pythagorean triplet in an array
def check_triplet(arr):
    arr = [ele * ele for ele in arr]
    arr.sort()

    for i in range(len(arr) - 1, 1, -1):
        left = 0
        right = i - 1

        while left < right:
            if arr[left] + arr[right] == arr[i]:
                return True
            elif arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1
    return False


# find number with freq 1, most brute force solution using linear search 0(n^2)
def find_freqone_brute(arr):
    # do linear search on each number
    for i in range(len(arr)):
        num = arr[i]
        cnt = 0
        for j in range(len(arr)):
            if arr[j] == num:
                cnt += 1
        if cnt == 1:
            return num


# slight better approach, use hash list to hash freq of elements 0(2*N),0(K), k is the largest from arr
def find_freqone_better(arr):
    maxele = arr[0]

    for ele in arr:
        maxele = max(maxele, ele)

    hash = [0] * (maxele + 1)

    for i in range(len(arr)):
        hash[arr[i]] += 1

    for i in range(len(arr)):
        if hash[arr[i]] == 1:
            return arr[i]


# find number with freq 1 in arr
def find_freqone(arr):
    freq = {}

    for ele in arr:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    for key, val in freq.items():
        if val == 1:
            return key


# another way, 2ptrs , find number with freq 1 from the array
def find_freqone2(arr):
    i = 0
    j = i + 1

    while i < len(arr) and j < len(arr):
        if arr[i] != arr[j]:
            return arr[i]
        i += 2
        j += 2


# most optimal using xor
def find_freqone_optimal(arr):
    xor = 0
    for ele in arr:
        xor ^= ele
    return xor


# find longest subarray with sum==k , most brute force =~ 0(n^3)
def find_subarray_brute(arr, k):
    n = len(arr)
    maxlen = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]

            if curr_sum == k:
                maxlen = max(maxlen, j - i + 1)
    return maxlen

# slight better approach, 0(N*logN)
def find_subarray_better(a,k):
    n = len(a) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen        

# prefix sum 1d brute force 

def prefix_sum_brute(arr):
    prefixsum=[0]*len(arr)
    for i in range(len(arr)):
        sum=0
        for j in range(0,i+1):
            sum+=arr[j]
        prefixsum[i]=sum 
    return prefixsum

# calculate prefix sum 1D 
def prefix_sum1d_better(arr):
    prefixsum=[0]*len(arr)
    prefixsum[0]=arr[0]
    
    for i in range(1,len(arr)):
        prefixsum[i]=prefixsum[i-1]+arr[i]
    return prefixsum

# prefix sum 2D brute force 
def prefix_sum2d_brute(arr):
    rows=len(arr)
    cols=len(arr[0])
    prefixsum=[[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            sum=0
            for r in range(i+1):
                for c in range(j+1):
                    sum+=arr[r][c]
            prefixsum[i][j]=sum 
    return prefixsum

# prefix sum 2D quite better 
def prefix_sum2d_better(arr):
    rows=len(arr)
    cols=len(arr[0])
    prefixsum=[[0]*cols for _ in range(rows)]
     
    
    for i in range(rows):
        for j in range(cols):
            top=prefixsum[i-1][j] if i>0 else 0
            left=prefixsum[i][j-1] if j>0 else 0 
            diag=prefixsum[i-1][j-1] if i>0 and j>0 else 0 
            prefixsum[i][j]=top+left-diag + arr[i][j]
    return prefixsum 

# for 1 based indexing 
def prefix_sum2d_better_1based(arr):
    rows=len(arr)
    cols=len(arr[0])
    
    prefixsum=[[0]*(cols+1) for _ in range((rows+1))]
    
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            prefixsum[i][j]=prefixsum[i-1][j]+prefixsum[i][j-1]-prefixsum[i-1][j-1]+arr[i-1][j-1]
    return prefixsum

# Find pivot index lc 724
def find_pivot_indexbrute(arr):
    n=len(arr)
    
    for i in range(n):
        if i==0: left=0
        if i==n-1: right=0 
        
        left=sum(arr[0:i])
        right=sum(arr[i+1:n])
        if left==right: return i 
    return -1 

# slight better approach with prefix sum 
def find_pivot_better(arr):
    # calculate prefix sum
    n=len(arr) 
    left=0
    total=sum(arr)
    for i in range(n):
        if (2*left+arr[i])==total:
            return i 
        left+=arr[i]
    return -1 
         
# Number of ways to split array , brute force , gives TLE 
def split_array_brute(arr):
    n=len(arr)
    cnt=0
    for i in range(n):
        if i==0: 
            left=arr[0]
        if i==n-1:
            return cnt 
        
        left=sum(arr[0:i+1])
        right=sum(arr[i+1:n])
        if left>=right: cnt+=1
        
# Number of ways to split array , better solution with prefix sum 
def split_array_better(arr):
    n=len(arr)
    right=sum(arr)
    left=0
    cnt=0
    
    for i in range(n-1):
        left+=arr[i]
        right-=arr[i]
        
        cnt+=1 if left>=right else 0
        
    return cnt 
def main():
    sys.stdin = open("arrays/input.txt", "r")
    sys.stdout = open("arrays/output.txt", "w")
    input = sys.stdin.readline

    # start here
    arr=list(map(int,input().split()))
    
    print(split_array_better(arr))

threading.Thread(target=main).start()
