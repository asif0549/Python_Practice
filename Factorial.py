def fact(num):
    if num <= 1:
        print(1, end="")
        return 1
    else:
        print(num, end=" x ")
        return num*fact(num-1)
num = int(input("Enter a number: "))
print(f" = {fact(num)}")