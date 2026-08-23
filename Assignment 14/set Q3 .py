#Q.3. Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set data type

lists = ["Apple", "banana", "Apple", "mango", "Grapes", "banana"]

unique_list = set(lists)

for word in unique_list:

    print(word, "=", lists.count(word))

print("Unique_words :", unique_list)
