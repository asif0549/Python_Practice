try:
    import array
    arr=array.array('i',[34,54,11,23,70])
    print(arr[5])

except Exception as e:
    print(e)
