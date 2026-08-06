#Right-Aligned Diamond Star Pattern♦️
num=int(input("Enter the number of rows for the diamond: "))
row=(num*2)-1
space=num-1
star=1
for i in range(row):
    for _ in range(space):
        print(" ",end=" ")
    for _ in range(star):
        print("*",end=" ")
    print()
    if i< num-1:
        star +=1
        space -=1
    else:
        star -=1
        space +=1
         
