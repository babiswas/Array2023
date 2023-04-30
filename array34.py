def rearrange_arr(arr):
    for i in range(len(arr)):
        if arr[i]>0 and arr[i]!=i:
            arr[arr[i]],arr[i]=arr[i],arr[arr[i]]

if __name__=="__main__":
    print("==================================")
    print("Rearranging the array:")
    arr=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    rearrange_arr(arr)
    print(arr)
    print("======================================")
