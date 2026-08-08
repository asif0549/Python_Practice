arr=input("Enter 2D array elements separated by spaces: ")
l=list(arr.split())
d={}
seen=set()
for i in l:
    if i not in seen:
        d[i]=l.count(i)
        seen.add(i)
print("Frequency of each element in the 2D array:")
print(d)