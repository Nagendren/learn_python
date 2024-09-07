# # Example 7

# for var1 in range(1,5):
#     for var2 in range(var1+1,5):
#         if (var1+var2)%2==0:
#             print('hi')
#             # Break the inner loop
#             break
#     else:
#         # Continue the outer loop if the inner loop wasn't broken
#         continue
#     print('hello')
#     # Inner loop was broken, now break the outer loop as well.
#     break

for var1 in range(1,3):
    print("I am from first for loop", var1)
    for var2 in range(var1+1,4):
        print('var1', var1)
        print('var2', var2)
        if ((var1+var2)%2==0):
            print("Iam Even bro!!")
            break
        else:
            print("I belong to if condition")
    else:
        print("I belongs to Second for loop")
print('End of both the For loop\'s')
