def allocate_pages(arr:list[int],k:int)->int:
    def find_stud(arr:list[int],mid:int)->int:
        sum=0
        num=0
        for i in arr:
            sum+=i
            if sum>mid:
               num+=1
               sum=i
        num+=1
        return num
    l,r=max(arr),sum(arr)
    while l<r:
        mid=(l+r)//2
        num=find_stud(arr,mid)
        if num==k:
            r=mid
        if num>k:
            l=mid+1
        elif num<k:
            r=mid-1
    return r

if __name__=="__main__":
    print("===================================")
    arr=[12, 34, 67, 90]
    min_pages=allocate_pages(arr,2)
    print(f"The minimum number of pages that should be allocated is {min_pages}")
    print("=====================================")

        

