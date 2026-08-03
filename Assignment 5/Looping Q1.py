#Q1. WAP to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter 
#credentials . let him try 3 times . After that program to terminate.

correct_id = "Harshadi"
correct_pass = "xyz123"
i = 0
while(i < 3):
   user_id = str(input("Enter User_id:"))
   password = str(input("Enter password:"))

   if(correct_id == user_id and correct_pass == password):
        print("Login successfully...!")
        break
   else:
        print("try again..")
        i +=1

if(i == 3):
    print("Maximum attempts exceeded, Program terminated.")    

    
 