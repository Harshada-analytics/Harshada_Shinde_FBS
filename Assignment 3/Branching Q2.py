#Q2. Write a program to input alphabet and check whether it is vowel or consonant.
 
alphabet = (input("Enter Character : "))

if (alphabet == "a" or alphabet=="e" or alphabet=="i" or alphabet=="o" or alphabet=="u" or 
    alphabet == "A" or alphabet=="E" or alphabet=="I" or alphabet=="O" or alphabet=="U"):
    print("Vowel")
else:
    print("Consonant")