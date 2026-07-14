#left half pyramid
rows=int(input("Enter no.of rows:"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()