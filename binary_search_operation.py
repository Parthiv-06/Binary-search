def bianry_search(arr,tar):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,3,4,5,6,7]
print(bianry_search(arr,6))