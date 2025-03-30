a= input("Enter the string to check anagram or not ")
b= input("Enter the 2nd string to check anagram or not ")

a=a.replace(" ","")
b=b.replace(" ","")

if sorted(a)==sorted(b):
    print(True)
else:
    print(False)