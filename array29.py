def find_pairs(arr:list[int],target:int)->tuple[int,int]:
    arr.sort()
    index1=0
    index2=len(arr)-1
    while index1<index2:
        num=target-arr[index1]
        if num==arr[index2]:
            return index1,index2
        elif num<arr[index2]:
            index2-=1
        elif num>arr[index2]:
            index1+=1
    return -1,-1
if __name__=="__main__":
    print("=============================")
    arr=[8, 7, 2, 5, 3, 1]
    index1,index2=find_pairs(arr,10)
    print("The indexes are:")
    print(index1,index2)
    print("=============================")
    if index1!=-1 and index2!=-1:
        print(arr[index1],arr[index2])
    print("===============================")
    

