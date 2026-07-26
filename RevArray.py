import numpy as np
def revArray(arr):
    n=len(arr)
    rev=np.empty(n,dtype=int)
    for j in range(n):
        rev[j]=arr[n-j-1]
    return rev

num=int(input("Enter size of an array: "))
arr=np.empty(num,dtype=int)
for i in range(num):
    arr[i]=(int(input(f"Enter element {i+1} : ")))
print("original array: ",arr)
print("Reversed array: ",revArray(arr))