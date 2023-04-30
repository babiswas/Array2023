def find_min_operations(arr):
    count=0
    for i in arr:
        if count%2!=0:
            i= not i
        if i==0:
            count+=1
    return count

if __name__=="__main__":
    print("=============================")
    arr=[1,0,1,0,0,0,1,1,0,0]
    print("The minimum operations to switch on all bulbs is:")
    num=find_min_operations(arr)
    print(f"The minimum operations to switch all bulbs on {num}")
    print("=================================")