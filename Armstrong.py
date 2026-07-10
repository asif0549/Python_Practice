num=int(input("Enter a number: "))
n=num
sum=0
while(num>0):
    rem = num % 10
    sum = sum + (rem*rem*rem)
    num = num //10
if n==sum:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")