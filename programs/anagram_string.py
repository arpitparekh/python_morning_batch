# check of both the Strings are anagram or not

str1 = input("Enter One String :")  # abc
str2 = input("Enter One String :")  # fdc   cdf

list1 = sorted(str1)
list2 = sorted(str2)

if list1==list2:
    print("Both the String are anagram")
else:
    print("Both the String are not anagram")
    
    
# list = [1,6,4,3,65,8,9,6,4,3,5,67,87]

# print(list.find(4))    

name = "Bascom"
print(name.find("c"))  # 3