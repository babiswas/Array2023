#Minimum time required to rpoduce m items

def min_time(arr:list[int],m:int)->int:
    '''Amout of time required to create m products'''
    time=0
    sum_product=0
    while True:
        for i in range(len(arr)):
            sum_product+=time//arr[i]
        if sum_product>=m:
            return time
        time+=1
        sum_product=0

if __name__=="__main__":
    print("============================")
    print("Minimum time required to create m products:")
    arr=[1,2,3]
    min_tm=min_time(arr,11)
    print(f"The minimum time required to create m products is {min_tm}")
    print("==============================")


