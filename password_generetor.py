from math import factorial
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
'E','F','H','I','J','K','L','K','L','M','N','O','P','Q','R','S',
'T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['+','<','"',"'",'*','/','&','[',']','}','{',';',':','$',
'#','!','^','.','>','?','|',',']

nl_letter=int(input("Enter how many letter do you want: "))
nl_number=int(input("Enter how many number do you want: "))
nl_symbo=int(input("Enter how many symbol do you want: "))

password_list=[]

for char in range(1,nl_letter+1):
    password_list .append(random.choice(letter))
for char in range (1,nl_number +1):
    password_list.append(random.choice(number))    
for char in range(1,nl_symbo + 1):
    password_list .append(random.choice(symbol))
random.shuffle(password_list)
password=''
for char in password_list:
    password += char
print("your password is this {}".format(password)) 