#Check if array elements are consiquitive.
#Figure out the minimum value in the array


def is_consiquitive(arr:list[int])->bool:
    index=arr.index(min(arr))
    num=0
    temp=arr[index]
    for i in range(len(arr)):
        num=num^temp^arr[i]
        temp+=1
    print(f"result {num}")
    if num==0:
        return True
    return False

if __name__=="__main__":
    print("=============================")
    print("Find if the list has consiquitive numbers:")
    l=[5,2,3,1,4]
    if is_consiquitive(l):
        print("There is consiquitive numbers in the array:")
    else:
        print("The array doesn't contain consiquitive numbers:")
    print("===============================")



    
