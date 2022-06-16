from http.client import CONTINUE
from msvcrt import LK_LOCK
from tracemalloc import stop
import string
from xml.dom.pulldom import CHARACTERS
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.punctuation)
s4=list(string.digits)

Characters_number= input("How many characters for the password ? : ")
while True:
    try:
        Characters_number = int(Characters_number)
        if Characters_number<6:
            print("U need at least 6 characters")
            Characters_number=input("How many characters for the password ? : ")
        else:
            break
    except:
        print("Please enter a number !")
        Characters_number= input("How many characters for the password ? : ")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(Characters_number*(30/100))
part2=round(Characters_number*(20/100))

password=[]
for i in range(0,part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(0,part2):
    password.append(s3[i])
    password.append(s4[i])

print("".join(password))




