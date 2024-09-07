# # Example 6

# for i in range (5,1,-1):
#     j=i
#     while(j==i):
#         print('hi', i*j)
#         i=i+1
#     if(i+j)>10:
#         continue
#     print(i**2)
# else:
#     print('For loop execution is successful')

for i in range(5,1,-1):
    print(i)
    j = i
    while(j==i):
        print('Multiplication of j * i is ', j*i)
        i=i+1
    if(i+j)>10:
        continue
    print(i**2)
else:
    print('For loop execution success')