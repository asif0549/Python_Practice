num=int(input("Enter a number: "))
x=num//2
n=num
sum=0
for i in range(1,x+1):
    if num%i==0:
        sum+=i
if (sum==n):
    print(f"{n} is Perfect Number.")
else:
    print(f"{n} is not a Perfect Number.")
