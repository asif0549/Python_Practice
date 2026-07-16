str=input("Enter a string:")
rev=""
for i in str:
    rev=i+rev
if str==rev:
    print(f"The string {str} is a palindrome -> {rev}")
else:
    print(f"The string {str} is not a palindrome -> {rev}")