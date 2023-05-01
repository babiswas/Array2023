#Range update of an array

def range_update(arr:list[int],l:int,r:int,val:int)->None:
    d=[0]*len(arr)
    for i in range(len(arr)):
        if i==0:
            d[i]=arr[i]
        else:
            d[i]=arr[i]-arr[i-1]
    print("========================================")
    print(arr)
    print(d)
    print("========================================")
    d[l]=d[l]+val
    d[r+1]=d[r+1]-val
    for i in range(len(arr)):
        if i==0:
            arr[i]=d[i]
        else:
            arr[i]=d[i]+d[i-1]
            d[i]=d[i]+d[i-1]
    print("======================================")
    print(arr)
    print(d)
    print("==========================================")

if __name__=="__main__":
    print("=============================")
    arr=[10, 5, 20, 40]
    range_update(arr,0,1,20)
    print(arr)
    print("==============================")

    