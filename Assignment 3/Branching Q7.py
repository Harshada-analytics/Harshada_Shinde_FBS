#Q7. Write a program to check if user had a entered correct userid and password.

import random 

user_id = (input("user_id : "))
password = (input("Password :"))

if(user_id == "admin" and password == "xyz123"):
    captcha = random.randint(1000,9999)
    print(f"Your captcha = {captcha}")

    chuser = int(input("Enter captcha =" ))

    if(chuser == captcha):
        print("User Login Successfully")
    else:
        print("Login Failed")
else:
    print("User is Invalid")
