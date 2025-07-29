import sys,re
sys.stdout=open("preprationSheet Sprint1 easy/output.txt","w")
sys.stdin=open("preprationSheet Sprint1 easy/input.txt","r")

# find missing number in a sequence 
def findMissing(seq):
    n=len(seq)+1
    totalSum=(n*(n+1))/2
    cursum=0
    for ele in seq: cursum+=ele 
    
    return int(totalSum-cursum)

# using bit manipulation (xor) 0(n) , 0(1)
def find_missing_xor(arr, n):
    xor_full = 0
    xor_arr = 0

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_full ^= i

    # XOR all elements in the array
    for num in arr:
        xor_arr ^= num

    # XOR of both gives the missing number
    return xor_full ^ xor_arr
        
# using sets 
def find_missing_sets(arr,n):
    full_set=set(range(1,n+1))
    
    return (full_set - set(arr)).pop()
    
n=int(input())
seq=list(map(int,input().split()))

print(find_missing_sets(seq,n))