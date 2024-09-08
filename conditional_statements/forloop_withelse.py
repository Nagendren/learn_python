# # The else block in a for loop is run if and only if the loop finishes normally without a break.
# # It's useful when you want to execute something at the end of the loop, but only if no break occurred.

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Loop finished without break")

# for i in range(5):
#     print(i)
# else:
#     print("Loop finished without break")

# Imagine you are searching for an item in a list. You want to do something 
# if you find the item (e.g., break the loop), but you also want to take action 
# if the item is not found. The else block is useful here because it will only run 
# if the loop finishes without finding (and breaking) the search.

my_list = [1, 2, 4, 5]

for item in my_list:
    if item == 3:
        print("Found 3!")
        break
else:
    print("3 not found in the list")
