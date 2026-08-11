n = int(input())
count = n * (n + 1) // 2
for i in range(n, 0, -1):
    for j in range(i):
        print(count, end="")

        count -= 1

        if j < i - 1:
            print("*", end="")
    print()