#if a number is divisible by the sum of its digits then it is called Harshad number
num=int(input("Enter a number: "))
n=num
sum=0
while num>0:
    rem=num%10
    sum=sum + rem
    num=num//10
if n % sum ==0:
    print(f"The number {n} is Harshar Number.")
else:
    print(f"The number {n} is not a Harshar Number.")