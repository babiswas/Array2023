def quick_select(arr,start,end,k):
    def partition(arr:list[int],start:int,end:int)->int:
        wall=start-1
        pivot=arr[end]
        for i in range(start,end):
            if arr[i]<pivot:
                wall+=1
                arr[wall],arr[i]=arr[i],arr[wall]
        wall+=1
        arr[wall],arr[end]=arr[end],arr[wall]
        return wall
    index=partition(arr,start,end)
    if index==k-1:
        return arr[index]
    elif index<k-1:
        return quick_select(arr,index+1,end,k)
    elif index>k-1:
        return quick_select(arr,start,end,index-1,k)
    
if __name__=="__main__":
    print("=========================")
    print("The kth smallest number is:")
    arr=[12,10,14,16,2,5]
    index=quick_select(arr,0,len(arr)-1,3)
    print(f"The kth smallest number is {index}")
    print("===========================")
    

    