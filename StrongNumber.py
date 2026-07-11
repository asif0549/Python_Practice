#The sum of factorials of the number is the number itself is known as strong number
fact = {
    0:1, 1:1, 2:2, 3:6, 4:24,
    5:120, 6:720, 7:5040,
    8:40320, 9:362880
}

num=int(input("Enter a Number: "))
n=num
sum=0
while(num>0):
    rem=num%10
    sum = sum + fact[rem]
    num=num//10

if (n==sum):
    print(f"The number {n} is Strong Number.")
else:
    print(f"The number {n} is not a Strong Number.")