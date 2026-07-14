rows=int(input("Enter no.of rows:"))
for i in range(rows-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()