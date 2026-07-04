num=int(input("Enter a number:"))
def fib(num):
    if num<=1:
        return num
    return fib(num-1)+fib(num-2)
for i in range(num):
    print(fib(i),end=" ")