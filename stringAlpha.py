str=input("Enter a String:")
char=list(str)
for i in range(len(char)):
    for j in range(i+1,len(char)):
        if ord(char[i]) > ord(char[j]):
            char[i],char[j]=char[j],char[i]
sorted="".join(char)
print(f"Sorted string in Alphabetical order : {sorted}")