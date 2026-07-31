#1 Reverse String
str = "ayush"
reversed_str = str[::-1]
print(reversed_str)

rev_str = "".join(reversed(str))
print(rev_str)

#2 Count "a" in the string
a = "Abhamasa"
a = a.count("a")
print(a)

b = "Apple Aam"
b = b.lower().count("a") #  because Python is case sensitive  
print(b)

#3 Check no is even or odd
a = int(input("Enter your no:"))
if (a%2 == 0):
    print("Even")
else:
    print("Odd")

#4 Number is positive negative or zero
a = int(input("Enter your no:"))
if (a>0):
    print("Positive")
elif(a<0):
    print("Negative")
else:
    print("Zero")

#5 Largest of the two numbers
a = int(input("First No: "))
b = int(input("Second No: "))

if(a>b):
    print(a)
else:
    print(b)

#6 Largest of 3 Numbers
a = int(input("First No: "))
b = int(input("Second No: "))
c = int(input("Third No: "))

if(a>b and b>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)

7 Student grading System
a = float(input("Enter Marks:"))

if(a>=90 and a<100):
    print("Grade: A")
elif(80<=a<=89):
    print("Grade: B")
elif(70<=a<=79):
    print("Grade: C")
elif(60<=a<=69):
    print("Grade: D")
else:
    print("Fail")

#8 Palindrome
a = input("Word: ")
a = a.lower()
b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("NOT Palindrome")