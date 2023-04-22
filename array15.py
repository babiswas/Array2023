import sys
def min_jumps_array(arr):
    steps=arr[0]
    count=0
    maxm=-sys.maxsize+1
    for i in range(1,len(arr)):
        steps-=1
        if maxm<arr[i]+i:
            maxm=arr[i]+i
        if steps==0 and i!=len(arr)-1:
            count+=1
            steps=maxm-i
    return count+1

if __name__=="__main__":
    print("=========================")
    print("Minimum jumps to the end of an array:")
    arr=[2,3,1,1,4]
    steps=min_jumps_array(arr)
    print(f"Minimum steps in to the end of array is {steps}")
    print("===========================")



