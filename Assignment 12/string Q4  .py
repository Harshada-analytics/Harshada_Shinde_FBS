#Q4. Pyhton Program to Form a new String where the first Character and last character have exchanged.

#string = "Harshada" # it's right 

string = input("Enter String : ")

new = string[-1] + string[1:-1] + string[0]      #a + arshad + H
                                                 # lats + middle + first
print(new)


#using funtion

def exchange(string):

    new = string[-1] + string[1:-1] + string[0]
    print(new)

string = input("Enter String: ")
exchange(string)