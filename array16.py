import sys
def min_jumps(arr:list[int])->int:
    def dfs(index:int):
        if index==len(arr)-1:
            return 0
        elif arr[index]==0:
            return sys.maxsize
        elif index+arr[index]>=len(arr)-1:
            return 1
        else:
            return min([dfs(i)+1 for i in range(index+1,index+arr[index]+1)])
    return dfs(0)
        
if __name__=="__main__":
    print("=========================")
    print("Minimum jumps to the end of an array:")
    arr=[2,3,1,1,4]
    steps=min_jumps(arr)
    print(f"Minimum steps in to the end of array is {steps}")
    print("===========================")


        