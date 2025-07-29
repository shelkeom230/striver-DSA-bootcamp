# find largest and smallest number in an array
def findnums(arr):
    return f'max: {max(arr)}, min: {min(arr)}'

# in one pass, optimised way (4 comparisons)
def findnums2(arr):
    l,r=0,len(arr)-1
    maxele,minele=float('-inf'),float('inf')
    while l<=r:
        for val in (arr[l],arr[r]):
            if val<minele:
                minele=val 
            if val>maxele:
                maxele=val 
        l+=1
        r-=1
    return f'max: {maxele} min: {minele}'

# most optimised way (1 pass, 1/2 comparisons for n elements = 1.5n)
def find_minmax(arr):
    n=len(arr)
    if n==0:
        return None,None 
    
    # initialise min and max 
    if n%2==0:
        if arr[0]<arr[1]:
            minimum,maximum=arr[0],arr[1]
        else:
            minimum,maximum=arr[1],arr[0]
        i=2
    else:
        minimum=maximum=arr[0]
        i=1
    
    # traverse in pairs
    while i<n-1:
        if arr[i]<arr[i+1]:
            local_min,local_max=arr[i],arr[i+1]
        else:
            local_min,local_max=arr[i+1],arr[i]
        
        if local_min<minimum:
            minimum=local_min
        if local_max>maximum:
            maximum=local_max
        i+=2
    
    return f'max: {maximum} min: {minimum}'
                    
n=int(input())
arr=[int(input()) for _ in range(n)]
print(find_minmax(arr))