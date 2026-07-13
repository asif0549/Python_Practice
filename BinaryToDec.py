#binary to decimal converter
def binary_to_decimal(binary):
    decimal = 0
    binary = str(binary)
    for i in range(len(binary)):
        bit = int(binary[-(i + 1)])
        decimal += bit * (2 ** i)
    return decimal
#print
binary=int(input("Enter a binary number: "))
print(f"The decimal value of {binary} is {binary_to_decimal(binary)}")