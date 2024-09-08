# 3.Write a program that will find all the numbers between 1000 and 3000 (both excluded) such that 
# each digit of a number is an odd number. Print the number of such elements

for i in range(1001,3000):
    if ((i%2)!=0):
        print(f"{i} is a ODD Number")
else:
    print("Printed all the ODD numbers between the range of 1000 - 3000, by excluding 1000 and 3000")
