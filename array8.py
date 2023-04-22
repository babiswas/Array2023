def rotate_array(arr,n):
    def reverse(arr,low,high):
        while low<=high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
    if n>=len(arr):
       raise Exception("Can't rotate")
    reverse(arr,len(arr)-n,len(arr)-1)
    reverse(arr,0,len(arr)-n-1)
    reverse(arr,0,len(arr)-1)
    return arr

if __name__=="__main__":
    print("=============================")
    print("Rotating the array:")
    arr=[1,2,3,4,5,6]
    rotate_array(arr,3)
    print(arr)
    arr=[1,2,3,4,5,6,7,8,9]
    print("Rotate an array")
    rotate_array(arr,7)
    print(arr)
    print("===========================")
