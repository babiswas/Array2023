def rearrange(arr):
    index=-1
    for i in range(len(arr)):
        if arr[i]<0:
            index+=1
            arr[i],arr[index]=arr[index],arr[i]
    index1=0
    index2=index+1
    while index1<len(arr) and index2<len(arr):
        if arr[index1]<0:
            arr[index1],arr[index2]=arr[index2],arr[index1]
            index2+=1
        index1+=2

if __name__=="__main__":
    arr=[4,5,6,7,8,-9,11]
    rearrange(arr)
    print(arr)


          
