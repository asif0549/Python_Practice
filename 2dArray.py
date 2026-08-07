#write a program to read the 2d array given
#no.of rows and cols and ele's store it and print squares
#of each ele in same order ?
'''
input:-

3
1 2 3
4 5 6
7 8 9

output:-
1 4 9
16 25 36
49 64 81
'''
row=int(input())
arr=[list(map(int,input().split())) for _ in range(row)]
for i in range(row):
    for j in range(row):
        print(arr[i][j]**2,end=" ")
    print()
print("-"*10,"Square of each element","-"*10)
for row in arr:
    for ele in row:
        print(ele**3,end=" ")
    print()
