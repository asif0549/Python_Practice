a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
x,y = a,b
while b > 0:
    a , b = b , a % b

hcf=a
lcm=(x * y)//hcf
print(f"LCM of {x} & {y} is: {lcm}")
print(f"HCF of {x} & {y} is: {hcf}")