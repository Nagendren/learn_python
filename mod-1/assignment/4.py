# 4.Write a program that accepts a string and calculates the number of letters and digits.
# Suppose if the entered string is: Edureka123 Then the output will be: LETTERS:- 7 DIGITS:- 3

my_string = "Edureka123"

output = { "LETTERS":0, "DIGITS":0 }

for i in my_string:
    if (i.isalpha()):
        print(f"{i} is a string")
        output["LETTERS"]+=1
        
    elif(i.isdigit()):
        print(f"{i} is a integer")
        output["DIGITS"]+=1
else:
    print(f"LETTERS:- {output['LETTERS']}, DIGITS:- {output['DIGITS']}" )