n1 = list(map(int, input("Enter List of numbers: ").split()))

print("Prime Numbers are:", end=" ")

for num in n1:
    if num < 2:
        continue

    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")