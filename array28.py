def find_pair(arr:list[int],target:int)->None:
    """Find all pairs which makes a target"""
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j])

if __name__=="__main__":
    print("=======================")
    print("Display all the targets:")
    arr=[1,5,7,-1]
    find_pair(arr,6)
    print("==========================")
