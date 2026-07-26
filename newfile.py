#to find minimum and maximum element of an array
import numpy as np
#user input for array elements
def FindMinMax(arr):
    min=max=arr[0]
    for i in arr:
        if i<min:
            min=i
        if i>max:
            max=i
            return min,max
num=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(num):
    arr.append(int(input(f"Enter element {i+1}: ")))
min_val, max_val = FindMinMax(arr)
print("Minimum element in the array is:", min_val)
print("Maximum element in the array is:", max_val)