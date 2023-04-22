import sys
def find_k_smallest(arr:list[int],k:int)->int:
    def find_diff(arr:list[int],mid:int)->int:
        index1=0
        index2=1
        num=0
        while index1<index2 and index2<len(arr):
            if arr[index2]-arr[index1]<=mid:
                num+=index2-index1
            else:
                while arr[index2]-arr[index1]>mid:
                    index1+=1
                num+=index2-index1
            index2+=1
        return num
    if len(arr)>=2:
        arr.sort()
        maxm=arr[len(arr)-1]-arr[0]
        minm=sys.maxsize-1
        index=0
        for i in range(1,len(arr)-1):
            if arr[i]-arr[index]<minm:
                minm=arr[i]-arr[index]
            index+=1
        while maxm>minm:
            mid=(maxm+minm)//2
            num=find_diff(arr,mid)
            if num>=k:
                maxm=mid
            elif num<k:
                minm=mid+1
        return maxm


if __name__=="__main__":
    print("=============================")
    arr=[1,2,3,4]
    index=find_k_smallest(arr,3)
    print(f"The {index} is the mid 3rd smallest diffence")
    print("=============================")




