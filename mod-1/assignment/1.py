# 1.Write a program to find the factors of a given  number 
# and check whether the factor is even or odd.Hint: 
# Use Loop with if-else statement

x = 5

for i in range(1,x+1):
    if ((i%2)==0):
        print(f'{i} is Even Number')
    else:
        print(f'{i} is Odd Number')

else:
    print(f"Completed finding Even and Odd number in the factors of {x}")


