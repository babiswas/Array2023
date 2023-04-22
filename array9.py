#Remove an element from an array to make it balanced

def balanced_array(arr:list[int])->int:
    sum_e=sum([val for index,val in enumerate(arr) if index%2==0])
    sum_o=sum([val for index,val in enumerate(arr) if index%2!=0])
    print(sum_e)
    print(sum_o)
    if sum_e==sum_o:
        print("The array is already balanced")
        return -1
    else:
        sm_o=0
        sm_e=0
        for index in range(len(arr)):
            if index%2==0:
                if sum_e-sm_e-arr[index]+sm_o==sm_e+sum_o-sm_o:
                    return index
                sm_e+=arr[index]
            elif index%2!=0:
                if sm_o+sum_e-sm_e==sm_e+sum_o-arr[index]-sm_o:
                    return index
                sm_e+=arr[index]
        return -1
    
if __name__=="__main__":
    print("============================")
    print("Find the index which if removed makes the array balanced:")
    arr=[5, 5, 2, 5, 8]
    index=balanced_array(arr)
    print(f"The index which represent equilibrium is {index}")
    print("=============================")


