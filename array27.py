import heapq
def k_frequent_element(arr:list[int],K:int)->None:
    record=dict()
    l=list()
    for i in arr:
        count=record.get(i,0)
        record.update({i:count+1})
    heapq.heapify(l)
    for key,value in record.items():
        heapq.heappush(l,(-value,key))
    while K>0:
        item=heapq.heappop(l)
        print(-1*item[0],item[1])
        K-=1

if __name__=="__main__":
    print("===========================")
    print("Find K frequent elements:")
    arr=[7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
    k_frequent_element(arr,4)
    print("=============================")




