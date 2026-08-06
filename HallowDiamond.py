n=int(input("Enter the number of rows: "))
rows=(n*2)-1
star=1
space=n-1
for i in range(rows):
    for _ in range(space):
        print(" ",end=" ")
    for k in range(star):
        if k==0 or k==star-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i < n-1:
        star +=2
        space -=1
    else:
        star -=2
        space +=1
