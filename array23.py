def find_missing_num(arr:list[int],n:int)->int:
    sm=(n*(n+1))//2
    return sm-sum(arr)

if __name__=="__main__":
    print("==========================")
    arr=[1,2,3,4,6,7,8,9,10,11,12]
    num=find_missing_num(arr,12)
    print(f"The missing number in an array is {num}")
    print("=============================")
