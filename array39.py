import sys
def find_max_diff(arr:list[int])->None:
    res=-sys.maxsize+1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            res=max(res,arr[j]-arr[i])
    return res

def find_diff(arr:list[int])->None:
    maxm=-sys.maxsize+1
    num=arr[0]
    minm=0
    for i in range(1,len(arr)):
        if (arr[i]-num)<0:
           num=arr[i]
        else:
            if arr[i]-num>maxm:
                maxm=arr[i]-num
    return maxm





if __name__=="__main__":
    print("==============================")
    print("find the maximum difference:")
    arr=[9,8,1,6,3,2]
    num=find_max_diff(arr)
    print(f"The maximum difference is:{num}")
    nm=find_diff(arr)
    print(f"The maximum difference is {nm}")
    print("=================================")
    arr=[9,8,6,3,2]
    nm=find_diff(arr)
    print(f"The maximum difference is {nm}")
    print("=================================")
    arr=[1,4,9,5,3,7]
    nm=find_diff(arr)
    print(f"The maximum difference is {nm}")
    print("====================================")




