ch=input("Enter a character: ")
ch=ch[0].lower()
if ch in ['a','e','i','o','u']:
    print(f"{ch} is vowel")
else:
    print(f"{ch} is consonant")