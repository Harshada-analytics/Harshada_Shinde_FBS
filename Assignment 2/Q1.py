#Q1. Convert the time entered in hh, min and seconds.

#input
time = int(input("Enter time in second :"))

#perform operation

hours = time // 3600
minute = (time % 3600) // 60
sec = time % 60

#Display result
print("Hours :", hours)
print("Minutes :", minute)
print("Seconds :", sec )
