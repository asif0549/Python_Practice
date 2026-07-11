num=int(input("Enter a number: "))
n=num
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if (sum>n): #if (sum<n)-> deficient number
    print(f"{n} is Abundant Number.")
else:
    print(f"{n} is not a Abundant Number.")
