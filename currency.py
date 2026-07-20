#a question asked in blackbucks
coin=[]
note=[]
num=int(input("Enter the currency amount: "))
for i in range(num):
    key,value=input("Enter the currency denomination and its value: ").split()
    value=int(value)
    if key=="coin":
        coin.append(value)
    else:
        note.append(value)
print("Coins : ")
for i in coin:
    print(i)
print("Notes :")
for i in note:
    print(i)
