num=int(input("Enter the number of rows for the rhombus: "))
for i in range(1,num+1):
    print(" "*(num-i)+"* "*i)
for j in range(num-1,0,-1):
    print(" "*(num-j)+"* "*j)