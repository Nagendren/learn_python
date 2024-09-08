# 4.Please write a program which accepts a string from console and print it in reverse order.
# Example: If the following string is given as input to the program: 
# welcome to edureka
# Then, the output of the program should be:
# akerude ot emoclew

x = input("Enter a word to get its reverse order: ")
word_length = len(x)
reverse = ""
for i in range(word_length):
    reverse_index = word_length-i-1    
    reverse = reverse + x[reverse_index]

print(reverse)

# Input_String=input("Enter a String : ")
# print(Input_String[::-1])
# print(''.join(reversed(Input_String)))