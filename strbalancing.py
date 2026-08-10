#Questioin asked in talent shine india
s=input("Enter String:").strip()
count=0
for ch in s:
    if ch=='L':
        count +=1
    else:
        count -=1
if count==0:
    print(f"{s} is balanced string")
else:
    print(f"{s} is not Balanced String")