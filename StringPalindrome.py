str=input("Enter a string: ")
rev=""
for ch in str:
    rev=ch+rev
if str==rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")