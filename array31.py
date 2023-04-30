import sys
def find_min_diff(arr):
    arr.sort()
    minm=sys.maxsize-1
    for i in range(len(arr)-1):
        temp=arr[i+1]-arr[i]
        if minm>temp:
            minm=temp
    return minm

if __name__=="__main__":
    print("================================")
    print("Minimum difference between pair of elements:")
    arr=[6,9,11,23,45,22,31,5,22]
    min_num=find_min_diff(arr)
    print(f"The minimum difference between pair of elements is {min_num}")
    print("==================================")
