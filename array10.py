def get_second_largest(arr:list[int])->int:
    first_largest=arr[0]
    second_largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>first_largest:
            second_largest=first_largest
            first_largest=arr[i]
        else:
            if arr[i]>second_largest:
                second_largest=arr[i]
    return second_largest

if __name__=="__main__":
    print("==========================")
    print("Display the second largest number in the array:")
    arr=[12,23,1,36,29,3,12,24]
    second_largest=get_second_largest(arr)
    print(f"The second largest number in an array is {second_largest}")
    print("===========================")


