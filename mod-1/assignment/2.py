# 2.Write a code that accepts a sequence of words as input 
# and prints the words in a sequence after sorting them alphabetically.
# Hint: Use split() to split the string into a list and then apply sort()

my_string = 'b c a f e g k j i'
words = my_string.split()
print(words)
words.sort()

for word in words:
    print(word)



# for i in words:
#     print(i)

# for i in my_string:
#     print(i)
