#Calculating the movie ticket price based on age and time of the show
#hacker rank constraints same price for matniee shows and evening shows for adults and children
age=int(input())
time=float(input())
if age > 0:
    match(time):
        case 10.15:
            if age >18:
                print("$5.00")
            else:
                print("$2.00")
        case 13.30:
            print("$2.00")
        case 18.00:
            if age >18:
                print("$5.00")
            else:
                print("$2.00")
        case 22.00:
            if age >=18:
                print("$5.00")
            else:
                print("$2.00")
else:
    print("Invalid age")