#Kadanes algorithm
import sys
def kadanes_algorithm(arr:list[int])->tuple[int,int,int]:

    '''Kadanes algorithm returns max subarrray sum,start_index,end_index'''
    
    maxm=-sys.maxsize+1
    sum_num=0
    start_index=0
    end_index=0
    index=0
    for i in range(len(arr)):
        sum_num+=arr[i]
        if sum_num>=0 and sum_num>maxm:
            maxm=sum_num
            start_index=index
            end_index=i
        elif sum_num<0:
            sum_num=0
            if i+1<len(arr):
                index=i+1
    return maxm,start_index,end_index

if __name__=="__main__":
    print("=========================")
    l=[-2,-3,4,-1,-2,1,5,-3]
    sum_num,start_index,end_index=kadanes_algorithm(l)
    print(sum_num,start_index,end_index)
    print(l[start_index:end_index+1])
    print("==========================")

