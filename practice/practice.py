# find floor and ceil of a target in an array
def findFloorAndCeil(arr,target,isCeil):
    start,end=0,len(arr)-1

    while start<=end:
        mid=(start+end)//2

        if target==arr[mid]:
            return mid
        elif target<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    if isCeil:
        return start
    else:
        return end

# find the index of first and last occurence of target in arr
def findIndex(arr,target):
    start,end=0,0
    startIdx,endIdx=None,None
    while start<len(arr)-1:
        if arr[start]==target:
            startIdx=start
            break
        start+=1

    while end>=0:
        if arr[end]==target:
            endIdx=end
            break
        end-=1
    return [startIdx,endIdx]

arr=[2,3,4,4,4,4,5,6,7,8]
target=4
print(findIndex(arr,target))