num=int(input("Enter a number:"))
for i in range(2,num):
    if num%i==0:
        print(f"{num} is not a prime number")
        break
print(f"{num} is prime")