# 9.Please write a program to randomly generate a list with 6 numbers, 
# which are divisible by 5 and 7, between 1 and 1500 inclusive.

import random

list1=[]
list2=[]

for i in range(1,1501):
    if i%35==0:
        list1.append(i)
        
for j in range(0,6):
    list2.append(random.choice(list1))

print(list2)