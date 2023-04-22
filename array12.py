def partition(arr,start,end):
    wall=start-1
    pivot=arr[end]
    for i in range(start,end+1):
        if arr[i]<pivot:
            wall+=1
            arr[wall],arr[i]=arr[i],arr[wall]
    wall+=1
    arr[wall],arr[end]=arr[end],arr[wall]
    return wall

def qsort(arr,start,end):
    if start<=end:
        index=partition(arr,start,end)
        qsort(arr,start,index-1)
        qsort(arr,index+1,end)

if __name__=="__main__":
    print("====================")
    print("Quicksort of an arry is:")
    arr=[12,10,3,23,2,17]
    qsort(arr,0,len(arr)-1)
    print(arr)
    print("======================")
