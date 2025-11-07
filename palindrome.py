p=input("Enter a string:")
rev=""
for i in p:
    rev=i+rev
if p==rev:
    print(p,"is a palindrome")
else:
    print(p,"is not palindrome")

#output:
'''
Enter a string:mam
mam is a palindrome
'''
    