num=int(input("Enter a number:"))
def fib(num):
    if num<=1:
        return num
    return fib(num-1)+fib(num-2)
for i in range(0,num+1):
    for j in range(i):
        print(fib(j),end=" ")
    print()