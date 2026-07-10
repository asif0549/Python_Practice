num=int(input("Enter a number: "))
n=num
sum=0
while(num>0):
    rem=num%10
    sum=sum * 10 + rem
    num = num//10

if (n==sum):
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")    