# 8.By using list comprehension, please write a program to 
# print the list after removing the 1st,3rd,5th numbers in [12,24,35,70,88,120,155].

my_list = [12,24,35,70,88,120,155]

new_list = []

for i in range(0,len(my_list)):
    if (i%2!=0):
        new_list.append(my_list[i])

print(new_list)