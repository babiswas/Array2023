def find_minm(arr:list[int])->int:
    l,r=0,len(arr)-1
    if arr[l]<arr[r]:
        return arr[l]
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>arr[mid+1]:
            return mid+1
        elif arr[mid]<arr[mid-1]:
            return mid
        else:
            if arr[mid]>=arr[l]:
                l=mid+1
            elif arr[mid]<=arr[r]:
                r=mid-1
    return -1

if __name__=="__main__":
    print("=========================")
    print("The minimum element in the array is:")
    arr=[4,5,6,7,8,1,2,3]
    index=find_minm(arr)
    print(arr[index])
    print("============================")
    
