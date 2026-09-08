def reverse_num(n):
    sign=-1 if n <0 else 1
    n=abs(n)
    reverse=int(str(n)[::-1])
    return sign * reverse



num=int(input("Enter a number: "))
n=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(f"The reverse of {n} is {rev}")
print(reverse_num(n))