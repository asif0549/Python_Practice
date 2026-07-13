#decimal to Hexadecimal converter
def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        decimal //= 16
    return hexadecimal
decimal=int(input("Enter a decimal number: "))
print(f"The hexadecimal value of {decimal} is {decimal_to_hexadecimal(decimal)}")