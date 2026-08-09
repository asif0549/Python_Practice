num=int(input("Enter a number:"))
l=len(n)
present=True
for i in range(l):
    for j in range(i+1,l):
        if n[i]==m[j]:
            present=False
            break
if present==True:
    print(f"The number {num} is unique")
else:
    print(f"The number {num} is not unique")