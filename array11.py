def find_min_max_page(arr:list[int],K:int)->int:

    def find_count(arr:list[int],mid:int)->int:
        sm=0
        count=0
        num=0
        for i in arr:
            sm+=i
            count+=1
            if sm>mid:
                num+=1
                sm=i
        if count==len(arr):
            num+=1
        return num
            
    low=max(arr)
    high=sum(arr)
    while low<high:
        mid=(low+high)//2
        num=find_count(arr,mid)
        if num==K:
            high=mid
        elif num>K:
            low=mid+1
        elif num<K:
            high=mid-1
    return mid

if __name__=="__main__":
    print("=====================")
    arr=[12, 34, 67, 90]
    min_pages=find_min_max_page(arr,2)
    print(f"The minimum number of pages that should be allocated is {min_pages}")
    print("========================")



    

