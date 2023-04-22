def bubble_sort(arr:list[int])->None:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__=="__main__":
    print("============================")
    print("Bubble sort algorithm is:")
    arr=[10,11,9,6,4,12,14,21,19]
    bubble_sort(arr)
    print(arr)
    print("==============================")


