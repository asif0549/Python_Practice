s = input("Enter a string: ")

words = s.split()

for i in words:
    if len(i) == 1:
        print(i.upper(), end=" ")
    else:
        print(i[0].upper() + i[1:-1] + i[-1].upper(), end=" ")