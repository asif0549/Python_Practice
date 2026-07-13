#program to print solid rectangle
def print_solid_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print_solid_rectangle(rows, cols)