def insertion_sort(arr:list[int])->None:
    for i in range(1,len(arr)):
        elem=arr[i]
        hole=i
        while hole>0:
            if arr[hole-1]>elem:
                arr[hole]=arr[hole-1]
                hole=hole-1
            else:
                break
        arr[hole]=elem

if __name__=="__main__":
    print("==============================")
    print("The insertion sort of the array is:")
    arr=[11,13,4,5,23,21,9,16]
    insertion_sort(arr)
    print(arr)
    print("===============================")