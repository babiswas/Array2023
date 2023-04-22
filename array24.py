def median_sorted(arr1:list[int],arr2:list[int])->int:

    """Median of two sorted array"""
    
    ln=len(arr1)+len(arr2)
    half=ln//2
    if len(arr2)<len(arr1):
        arr1,arr2=arr2,arr1
    low,high=0,len(arr1)
    while True:
        index=(low+high)//2
        index2=half-index-2
        Aleft=arr1[index] if index>=0 else float("-infinity")
        Aright=arr1[index+1] if index+1<len(arr1)+1 else float("infinity")
        Bleft=arr2[index2] if index2>=0 else float("-infinity")
        Bright=arr2[index2+1] if index2+1<len(arr2) else float("infinity")
        if Aleft<=Bright and Bleft<=Aright:
            if ln%2:
                return min(Aright,Bright)
            else:
                return (min(Aleft,Bleft)+(Aright,Bright))//2
        elif Aleft>Bright:
             high=index-1
        elif Bleft>Aright:
             low=index+1

#Median of two sorted arrays
if __name__=="__main__":
    print("========================")
    A=[11,12,13,14,15,16]
    B=[1,2,3,4,5,6,7]
    index=median_sorted(A,B)
    print(f"The median of the array is {index}")
    print("==========================")


