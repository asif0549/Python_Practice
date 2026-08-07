row=int(input("Enter number of rows: "))
for i in range(row):
    for j in range(i+1):
        if (i+j)%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()