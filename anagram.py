str1=input("Enter first string:")
str2=input("Enter second string:")
str1=str1.replace(" ","").lower()
str2=str2.replace(" ","").lower()
if sorted(str1)==sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are mot anagrams")

#output:
'''
Enter first string:silent
Enter second string:listen
The strings are anagrams
'''