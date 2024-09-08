# 6.With two given lists [1,5,10,12,34,13] and [4,7,8,10,5,13,24], 
# write a program to make a list whose elements are intersection of the above given lists.

list1=[1,5,10,12,34,13] 
list2=[4,7,8,10,5,13,24]

list1_intersect_list2=list(set(set(list1)&set(list2)))
print(list1_intersect_list2)
print(sorted(list1_intersect_list2))
