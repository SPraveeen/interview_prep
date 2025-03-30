from collections import Counter
a= input("Enter the string to check anagram or not ")
b= input("Enter the 2nd string to check anagram or not ")

count1=Counter(a)
count2=Counter(b)

if count1==count2:
    print(True)
else:
    print(False)