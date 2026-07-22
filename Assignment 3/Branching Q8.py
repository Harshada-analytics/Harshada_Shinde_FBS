#Q8. Write a program to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number and ask user to enter the same. 
# If user enters the same nmber then show him success message otherwise failed.(something like captcha)
  
import random 

userid = (input("Enter User_id : "))
password = (input("Enter Password :"))

if(userid == "Admin" and password == "xyz@123"):
    captcha = random.randint(1000,9999)
    print(f"your captcha = {captcha}")

    chuser = int(input("Enter captcha:"))
      
    if(chuser == captcha):
        print("Loging Successful..!")
    else:
        print("Login Failed")
else:
    print("Invalid user")