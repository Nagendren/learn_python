# Iteration using for loop

# # Example 5

# for i in range(1,5):
#     print(i)
#     for j in range(i,i+2):
#         if((i+j)%2==0):
#             print('Hello')
#         else:
#             continue

for i in range(1,5):
    print(f"from First loop {i}")
    for j in range(i,i+2):
        if((i+j)%2==0):
            print(f"Even number = {j}")
        else:
            print(f"Odd number {j}")
