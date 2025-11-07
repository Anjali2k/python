#Ex 1:
#Prime Numbers
prime=int(input("Enter a number:"))
if prime<=0:
    print(prime,":Not a prime Number")
elif prime==2:
    print(prime,":Prime Number")
else:
    for i in range(2,prime-1):
        if prime%i!=0:
            print(prime,":Prime Number")
            break
        else:
            print(prime,":Not prime Number")
            break

#output:
'''
Enter a number:78
78 :Not prime Number
'''