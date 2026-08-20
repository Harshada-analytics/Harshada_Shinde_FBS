#Q3. Python Program to Detect if Two Strings are Anagrams

string1 = input("Enter String1 : ")
string2 = input("Enter String2 : ")      

if sorted(string1) == sorted(string2):
    print("String is Anagram")
else:
    print("String is Not Anagram")