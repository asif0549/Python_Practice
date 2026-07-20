num=int(input("Enter the number of rows for the pyramid: "))
for i in range(1,num+1):
    print(" "*(num-i)+"* "*i)
print()