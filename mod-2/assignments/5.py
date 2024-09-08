# 5.Please write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program:
# xyzXabcabd
# Then, the output of the program should be:
# x 1
# y 1
# z 1
# X 1
# a 2
# b 2
# c 1
# d 1

Input_String=input("Enter a String ")

for i in range(0,len(Input_String)):
    count=1
    for j in range(i+1,len(Input_String)): #(1,5)
        if(Input_String[j]!="?"):
            if Input_String[j]==Input_String[i]:
                count+=1
    if(count>1):
        print(Input_String[i],count)
        Input_String=Input_String.replace(Input_String[i],"?")
    elif(count==1):
         if(Input_String[i]!='?'): 
            print(Input_String[i],count)

