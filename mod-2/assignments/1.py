# 1.Smith wants to register to a bus booking website for booking bus tickets. For this registration, 
# he needs to provide user-id and password. 
# There are some built-in rules for checking the validity of the passwords entered by the users.
# Following are the rules for checking the validity of a password:

# i.	At least 1 alphabet
# ii.	At least 1 digit between [0-9]
# iii.	At least 1 character from [@&]
# iv.	Minimum length of transaction password: 5
# v.	Maximum length of transaction password: 10


print("Welcome to login page")

userid = input("Enter your userid : ")
password = input("Enter your password : ")

letter_check = False
digit_check = False
length_check = False
character_check = False
capital_check = False

pass_length = len(password)

for i in password:
    if(i.isalpha):
        letter_check = True
        break
for i in password:
    if(i.isdigit):
        digit_check = True
        break
if (len(password) >=5 and len(password) <=10):
    length_check = True

for i in password:
    if i in ['@','&']:
        character_check = True
        break

for i in password:
    if (i.isupper()):
        capital_check = True
        break

# Another way of capital check 
# if (any(i.isupper() for i in password)):
#     capital_check = True

if (length_check and digit_check and length_check and character_check and capital_check):
    print("You passed the check")
else:
    print("you failed the check")

