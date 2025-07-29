import sys
sys.stdout=open("preprationSheet Sprint1 easy/output.txt","w")
sys.stdin=open("preprationSheet Sprint1 easy/input.txt","r")

# find median of an array of integers 
def mergeSort():
    pass 
def findMedian(arr):
    arr=sorted(arr)
    
    # 2. find median 
    n=len(arr)
    # n is odd 
    if n%2==1:
        return arr[(n//2)]
    # n is even 
    else: 
        mid1=arr[n//2]
        mid2=arr[n//2 -1]
        return (mid1+mid2)//2


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    
    print(findMedian(arr))