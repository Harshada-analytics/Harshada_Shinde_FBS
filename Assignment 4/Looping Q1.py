#q.1 WAP to print all even number until n.

num = int(input("Enter Number :"))

i = 1
while(i <= num):
    if(i % 2 == 0):
        print(i)
        i += 1


# Or (outcome will same)

num = int(input("Enter Number :"))
i = 2

while(i <= 20):
    if(i % 2 == 0):
        print(i)
        i += 1