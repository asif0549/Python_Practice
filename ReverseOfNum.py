num=int(input("Enter a number: "))
n=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(f"The reverse of {n} is {rev}")