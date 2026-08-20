#Q2. Python program to remove the nth index charater from a Non-Empty String.

string = "ABCDEFGH"
new = ""

index  = int(input("Enter Index: "))

for i in range(len(string)):

     if i == index :
          continue 
     else:
          new += string[i] 

print (new)