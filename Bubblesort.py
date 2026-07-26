import numpy as np
def Bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr      
arr=[]
num=int(input("Enter the size of Array: "))
for i in range(1,num+1):
    arr.append(int(input(f"Enter element {i}: ")))
Sorted_arr=Bubblesort(arr)
print("Sorted Array: ",Sorted_arr)
