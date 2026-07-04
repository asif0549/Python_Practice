number=int(input("ENter a number:"))
n=number
sum=0
while number>0:
    num=number%10
    sum+=num
    number=number//10
print(f"The sum of the digits of {n} is {sum}")