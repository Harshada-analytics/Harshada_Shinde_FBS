#Q 2. Python Program to Concatenate Two Dictionaries Into One

student1= { 
        "first_name" : "Rahul",
        "last_name" : "Sharma"
}

student2 = {
    "city": "Pune",
    "age": 20
 }

total = {**student1,**student2}

print(total)