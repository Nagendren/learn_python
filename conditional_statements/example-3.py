# Example 3:
# a=10
# b=15.0
# c=a+b
# if(type(c) is int):
#     print('It is an integer')
# elif(type(c) is float):        #Line1
#     print('It is a float')
# elif(type(c) is float):        #Line2
#     print('Yes, it is a float')
# else:
#     print('The datatype of c is:', type(c))

a = 10
b = 15.0

c = a + b

print(c)
print(type(c))

if(type(c) is int):
    print(f"It's an Integer type. value of c is {c} and it type is {type(c)}")

elif(type(c) is float):
    print(f"It's an float type. value of c is {c} and it type is {type(c)}")

elif(type(c) is float):
    print("Yes!!!! It's an float type")