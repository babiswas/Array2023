def find_triplet(arr:list[int])->int:
    counter=0
    index=[0]*1000
    for i in arr:
        index[i]=1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if index[arr[i]+arr[j]]==1:
                print(arr[i],arr[j],arr[i]+arr[j])
                counter+=1
    return counter

if __name__=="__main__":
    print("==========================")
    arr=[12, 3, 4, 1, 6, 9]
    num=find_triplet(arr)
    print(f"The number of triplets is {num}")
    print("===========================")



                

