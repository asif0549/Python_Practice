import numpy as np

try:
    N = int(input("Enter the number of elements in the array: "))
    lst = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    n, m = map(int, input("Enter the number of rows and columns separated by space: ").split())
except EOFError:
    print("Error: Input was not provided.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    if len(lst) != N:
        print("Error: The declared element count does not match the values entered.")
    elif N != m * n:
        print("Error: The number of elements does not match the specified dimensions.")
    else:
        arr = np.array(lst).reshape(n, m)
        print("The 2D array is:")
        for row in arr:
            print(*row)