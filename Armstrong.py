num=int(input("Enter a number: "))
n=num
p=len(str(num))
sum=0
while(n>0):
    rem = num % 10
    sum = sum + (rem**p)
    num = num //10
if n==sum:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")