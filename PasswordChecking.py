#password verification
st=input("Enter Password: ")
special="~!@#$%^&*"
invalid=" "
if len(st)< 8 and st[0] in invalid and st.isdigit():
    print("Password should contain atleast 8 characters")
elif st[0].isupper() and st[1:].islower() and st in special and st.isalnum():
    print(f"{st} is valid")
else:
    print("Invalid Password")
    