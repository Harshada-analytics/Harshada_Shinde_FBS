#Q.3 python program to check if a given key Exists iin a dictionary or not.

key = input("Enter key :")

student = {
      "id" : 101,
      "name" : "Ganesh",
      "Last" : "Patil"
}

if key in student:
     print("Key is Available")
else:
    print("Key is not Available")