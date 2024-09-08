#3.Please write a program which accepts a string from console and 
# print the characters that have even indexes if the character is an alphabet. 
# Concatenate the characters and print.

# eesha18
# 0123456

my_string = "Ed12ur3ka1Python12"

con = ""

for i in range(len(my_string)):
    if (i%2==0 and my_string[i].isalpha()):
        con = con + my_string[i]
    
print(con)

# Input_String=input("Enter a String")
# Output_String=""
# for i in range(0,len(Input_String)):
#     if(i%2==0 and Input_String[i].isalpha()==True):
#         Output_String=Output_String+Input_String[i]
# print(Output_String) 

    