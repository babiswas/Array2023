#Peak element in an array

def find_peak_element(arr:list[int])->int:
        start,end=0,len(arr)-1
        while start<end:
            mid=(start+end)//2
            if mid!=0 and mid!=len(arr)-1:
                if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                    return mid
                elif arr[mid]<arr[mid-1]:
                    end=mid-1
                elif arr[mid]<arr[mid+1]:
                    start=mid+1
            elif mid==0:
                if arr[mid]>arr[mid+1]:
                    return mid
                else:
                    start=mid+1
            elif mid==len(arr)-1:
                if arr[mid]>arr[mid-1]:
                    return mid
                else:
                    end=mid-1
        return -1

if __name__=="__main__":
    print("=========================")
    print("Find the peak element in an array:")
    arr=[5,10,20,15]
    index=find_peak_element(arr)
    print(f"The peak element in an array is {arr[index]}")
    print("===========================")

