# Example 2:

# var1=10
# var2=15
# if(var1>=var2):
#     if((var1-var2)%2==0):
#         print('Welcome to Edureka')
#     else:
#         print('Hello Edureka')
# else:
#     if((var2-var1)%2==0):
#         print('Welcome to Python')
#     else:
#         print('Hello Python')

var1 = 13
var2 = 13
if (var1 > var2):

    print(f"var1 = {var1} is greater than var2 = {var2}")

    if((var1-var2)%2==0):
        print('It\'s an Even Number')
    else:
        print("It's an Odd Number")

elif (var2 > var1):
    print(f"var2 = {var2} is greater than var1 = {var1}")

    if((var2-var1)%2==0):
        print("It's an Even number")
    else:
        print("It's an Odd Number")
else:
    print(f"Var1 = {var1} is equal to var2 = {var2}")

    if((var1-var2)%2==0):
        print("It's an Even number")
    else:
        print("It's an Odd Number")

