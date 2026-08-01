#checking the IFSC code validity and fetching bank details using the IFSC code.
#Constraints
#string length must be 11
#1st four values must be upperface
#5th value should 0
#rest for values are alphanumeric 
num=int(input("Enter the nu.of IFSC Codes: "))
for i in range(num):
    str=input(f"Enter IFSC CODE {i+1}: ")
    if (len(str)==11 and str[:4].isalpha() and str[:4].isupper() and str[4]=='0' and str[5:].isalnum()):
        print(f"{str} is valid IFSC Code")
    else:
        print(f"{str} is in valid IFSC Code")