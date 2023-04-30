import sys
def minimum_platforms(arr1,arr2):
    arr1.sort()
    arr2.sort()
    index1=0
    index2=0
    count=0
    maxm=-sys.maxsize+1
    while index1<len(arr1) and index2<len(arr2):
        if arr1[index1]<arr2[index2]:
            count+=1
            if count>maxm:
                maxm=count
            index1+=1
        elif arr1[index1]>arr2[index2]:
            count-=1
            index2+=1
    return maxm

def min_platform(arr,dep):
    platform=0
    result=0
    for i in range(len(arr)):
        platform=1
        for j in range(len(arr)):
            if i!=j:
                if (arr[i]>=arr[j] and arr[i]<=dep[j]) or  (arr[j]>=arr[i] and arr[j]<=dep[i]):
                    platform+=1
        result=max(result,platform)
    return result


if __name__=="__main__":
    print("==============================")
    print("The minimum number of platforms required:")
    arr1=[900,940,950,1100,1500,1800]
    arr2=[910,1200,1120,1130,1900,2000]
    num=minimum_platforms(arr1,arr2)
    print(f"The minimum number of platforms required is {num}")
    print("===================================")
    print("The minimum number of platforms required:")
    arr1=[900,940,950,1100,1500,1800]
    arr2=[910,1200,1120,1130,1900,2000]
    num=min_platform(arr1,arr2)
    print(f"The minimum number of platforms required is {num}")

