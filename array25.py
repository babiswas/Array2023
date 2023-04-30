def find_subarray(arr:list[int],allsum:int)->tuple[int,int,int]:
    index1=0
    index2=0
    sm=0
    while index1<len(arr) and index2<len(arr) and index1<=index2:
        sm+=arr[index2]
        if sm==allsum:
            return index1,index2,sm
        elif sm>allsum:
            while sm>allsum:
                sm-=arr[index1]
                index1+=1
            if sm==allsum:
                return index1,index2,sm
        index2+=1
    index1=0
    return index1,-1,-1

def find_mysubarray(arr:list[int],allsum:int)->tuple[int,int]:
    sm=0
    for i in range(len(arr)-1):
        sm+=arr[i]
        for j in range(i+1,len(arr)):
            sm+=arr[j]
            if sm>allsum:
                break
            if sm==allsum:
                return i,j
        sm=0
    if sm!=allsum:
        sm=0
        sm+=arr[-1]
        if sm==allsum:
            return len(arr)-1,len(arr)-1
    return 0,-1


if __name__=="__main__":
    print("===========================")
    arr=[1,4,20,3,10,5]
    num1,num2,num3=find_subarray(arr,33)
    if num2!=-1:
       print(arr[num1:num2+1])
       print(num1,num2)
    print("============================")
    print("Second method of finding subarray:")
    num1,num2=find_mysubarray(arr,33)
    print(num1,num2)
    print("=============================")

