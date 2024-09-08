import base64
my_id = input("Enter your UniqueID : ")

myid_len = len(my_id)

length_check = False
digit_check = False

if (myid_len == 10):
    length_check = True

for i in range(0,myid_len):
    print(my_id)
    if my_id.isdigit():
        digit_check = True

if (length_check and digit_check):
    print("Your ID is Valid")
    my_id_encrypt = base64.b64encode(my_id.encode())
    print(my_id_encrypt)
    my_id_decrypt = base64.b64decode(my_id_encrypt)
    print(my_id_decrypt)
else:
    print("Your ID is not Valid")

