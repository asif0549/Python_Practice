a=int(input("Enter numerator of first fraction: "))
b=int(input("Enter denomerator of first fraction:"))

c=int(input("Enter numerator of second fraction: "))
d=int(input("Enter denomerator of second fraction:"))

num=(a * d) + (c * b)
den= b * d
print(f"The Addition of fractions is: {num}/{den} = {num/den:.2f}")