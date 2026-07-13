#Decimal to octal conversion
def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal
decimal=int(input("Enter a decimal number: "))
print(f"The octal value of {decimal} is {decimal_to_octal(decimal)}")