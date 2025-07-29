# bubble sort  
def bubbleSort(arr):
    n=len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr 

# selection sort 
def selectionSort(arr):
    for i in range(len(arr)):
        minele=i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minele]:
                minele=j 
        arr[i],arr[minele]=arr[minele],arr[i]
    return arr 

# insertion sort 
def insertionSort(arr):
    n=len(arr)
    
    for i in range(n):
        j=i 
        
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr 

# merge function 
def merge(arr,low,mid,high):
    left,right=low,mid
    temp=[]
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
            
    # append remaining elements 
    while left<=mid:
        temp.append(arr[left])
        left+=1
    
    while right<=high:
        temp.append(arr[right])
        right+=1
    
    # copy back temp to arr 
    for i in range(len(temp)):
        arr[i+low]=temp[i]
        
# merge sort 
def mergeSort(arr,low,high):
    if low>high: return 
    mid=low+(high-low)//2
    
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr 
if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(mergeSort(arr,0,len(arr)))