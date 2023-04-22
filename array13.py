def find_subset(arr:list[int],n:int,k:int,num:int)->int:
    if n==0:
        return 0
    elif num>k:
        return 0
    else:
        if n-1>=0 and arr[n-1]<=k and num*arr[n-1]<=k:
            return 1+find_subset(arr,n-1,k,num*arr[n-1])+find_subset(arr,n-1,k,num)
        else:
            return find_subset(arr,n-1,k,num)
        
if __name__=="__main__":
    print("============================")
    print("The number of subset with value less than k:")
    arr=[2,4,5,3]
    num=find_subset(arr,len(arr),12,1)
    print(num)
    print("===============================")





    
