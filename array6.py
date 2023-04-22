def min_time(arr:list[int],m:int)->int:
    def find_items(arr:list[int],tm:int)->int:
        num=0
        for i in arr:
            num+=tm//i
        return num
    
    min_time=1
    max_time=m*arr[0]
    while min_time<=max_time:
        mid=(min_time+max_time)//2
        items=find_items(arr,mid)
        if items<m:
            min_time=mid+1
        elif items>m:
            max_time=mid
        elif items==m:
            return mid
    return -1

if __name__=="__main__":
    print("============================")
    print("Minimum time required to create m products:")
    arr=[1,2,3]
    min_tm=min_time(arr,11)
    print(f"The minimum time required to create m products is {min_tm}")
    print("==============================")


