import sys
def find_missing(arr,m):
    start,end=0,len(arr)-1
    if arr[start]!=0:
        return 0
    minm=sys.maxsize-1
    for i in range(len(arr)-1):
        if arr[i]+1!=arr[i+1]:
            if minm>arr[i]+1:
                minm=arr[i]+1
                return minm
    if arr[len(arr)-1]!=m-1:
        return m-1

if __name__=="__main__":
    print("================================")
    print("Find the missing number in an arry:")
    arr=[0, 1, 2, 3, 4, 5, 6, 7, 10]
    num=find_missing(arr,10)
    print(f"The missing number is {num}")
    print("===================================")

