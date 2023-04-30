def kadanes_algo(arr:list[int])->tuple[int,int,int]:
    '''Kadanes algorithm'''
    sm=0
    maxm=-999
    start_index=0
    end_index=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sm+=arr[j]
            if maxm<sm:
                maxm=sm
                start_index=i
                end_index=j
        sm=0
    return maxm,start_index,end_index

if __name__=="__main__":
    print("=====================")
    print("Kadanes Algorithm:")
    arr=[2,-3,4,-1,-2,1,5,-3]
    num1,num2,num3=kadanes_algo(arr)
    print(f"The maxm sum is {num1}")
    print(num2,num3)
    print("========================")