str=input("Enter a string: ")
char=list(str)
for i in range(len(char)):
    if ord(char[i])>=65 and ord(char[i])<=90:
        char[i]=char[i].lower()
    elif ord(char[i])>=97 and ord(char[i])<=122:
        char[i]=char[i].upper()
print("Toggled string is :","".join(char))