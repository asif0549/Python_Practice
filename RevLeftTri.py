rows=int(input("Enter no.of rows:"))
for i in range(rows-1,0,-1):
    print(" "*(rows-i-1),end=" ")
    for j in range(i):
        print("*",end="")
    print()