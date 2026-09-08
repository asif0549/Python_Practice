def count_set_bits(n):
    count=0
    while n >0:
        n=n&(n-1)
        count +=1
    return count
num=int(input())
count_set_bits(num)