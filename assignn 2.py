maxparticipants = int(input("Enter total no of Tickets available"))
import random
a=[]
for i in range(maxparticipants):
    a=input("Enter name of participants:")
b=(random.randint(0,maxparticipants-1))
print("The winner is: ",a)
