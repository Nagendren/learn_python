# 5.Design a code which will find whether the given number is Palindrome number or not

# input_number=int(input("Enter a number:"))
# temp_num=input_number
# reverse=0
# while(input_number>0):
#     digit=input_number%10 #1
#     reverse=reverse*10+digit #1
#     input_number=input_number//10
# if(temp_num==reverse):
#     print(temp_num," is palindrome")
# else:
#     print(temp_num," is not a palindrome!")

#Below code will detect both numbers and words

word = "12345"

l = len(word)

palindrome_flag = False

for i in range(l):
    if word[i] != word[l-i-1]: #[6-0-1]
        palindrome_flag = False
        break
    else:
        palindrome_flag = True
if (palindrome_flag):
    print(f"it's a planidrome {word}")
else:
    print(f"it's NOT a planidrome {word}")
