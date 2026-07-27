#WAP to input user's first name & print its length
a=input("First Name: ")
len1=len(a)
print("Length of your Name: ", len1)

#WAP to find the occurrence of '$' in a String.
str="Hi, $Iam the $ symbol $99.99"
a=str.count("$")
print(a)

#WAP to check if a number entered by the user is odd or even
num = int(input("Enter the number: "))
rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

#WAP to find the greatest of 3 numbers entered by the user.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a >= b and a >= c):
    print("First no is largest", a)
elif(b >= c):
    print("Second no is largest", b)
else:
    print("third no is largest", c)

#WAP to check if a number  is a multiple of 7 or not
num = int(input("Enter the number: "))
rem = num % 7
if(rem == 0):
    print("Multiple of 7")
else:
    print("Not multiple of 7")

