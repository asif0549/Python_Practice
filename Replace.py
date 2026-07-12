ll=list(map(int,input("Enter the numbers: ").split()))
for i in range(len(ll)):
    if ll[i]==0:
        ll[i]=1
print(f"The numbers after replacing 0 with 1 are: {ll}")