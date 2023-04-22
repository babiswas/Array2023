def binary_search(arr:list[int],key:int)->int:
    '''Binary search for a key'''
    start,end=0,len(arr)
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            end=mid-1
        elif arr[mid]<key:
            start=mid+1
    return -1

if __name__=="__main__":
    print("========================")
    print("Binary search of the array")
    arr=[11,13,15,19,21]
    index=binary_search(arr,19)
    print(f"The binary search of the array is:{index}")
    print(f"The searched element is {arr[index]}")
    print("===========================")

