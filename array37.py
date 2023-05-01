def difference(arr:list[int])->None:
    print("============================")
    #Difference array
    print(arr)
    d=[0]*len(arr)
    for i in range(len(arr)):
        if i==0:
            d[i]=arr[i]
        else:
            d[i]=arr[i]-arr[i-1]
    print("==============================")
    print(d)
    for i in range(len(arr)):
        if i==0:
            d[i]=d[i]
        else:
            d[i]=d[i]+d[i-1]
    print(d)
    print("===============================")

if __name__=="__main__":
    print("=============================")
    arr=[12,14,16,11,29,12,13]
    difference(arr)
    print("==============================")

    