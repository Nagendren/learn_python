# 7.By using list comprehension, please write a program to print the list 
# after removing the values which are divisible by 6 in [12,24,35,24,88,120,155].

my_list = [12,24,35,24,88,120,155]

new_list = []

for i in range(len(my_list)):
    if (my_list[i]%6!=0):
        new_list.append(my_list[i])
print(f"Removed values divided by 6 \nfollowing is the new list which are non divisible by 6 \n{new_list}")

# list1=[12,24,35,24,88,120,155]
# list2=[i for i in list1 if i%6!=0]
# print(list2)