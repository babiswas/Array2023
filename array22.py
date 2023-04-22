def triplet(arr:list[int])->int:
    counter=0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if (arr[i]+arr[j]==arr[k]) or (arr[j]+arr[k]==arr[i]) or (arr[k]+arr[i]==arr[j]):
                    print(arr[i],arr[j],arr[k])
                    counter+=1
    return counter

if __name__=="__main__":
    print("============================")
    arr=[12, 3, 4, 1, 6, 9]
    num=triplet(arr)
    print(f"The number of triplets is {num}")
    print("============================")

                
