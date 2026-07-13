#decimal to binary converter
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary
decimal=int(input("Enter a decimal number: "))
print(f"The binary value of {decimal} is {decimal_to_binary(decimal)}")