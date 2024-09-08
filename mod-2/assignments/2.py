# 2.Write a program for printing all elements of a list and their indexes in the list. 
# Take the list as a user input.

user_list = list(input("Enter your list : "))

user_len = len(user_list)

for i in range(user_len):
    print(user_list[i] , i+1)

# a=[]
# number_of_elements=eval(input("enter"))
# print("enter elements now")
# for i in range(0,number_of_elements+1):
#     a.append(int(input("enter")))
# for elem in range(0,len(a)):
#     print(elem, str(a[elem]))
