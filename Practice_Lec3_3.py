#1. Check eligible for vote 
age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible")
else:
    print("NOT Eligible")

#2. Check for Leap year
year = int(input("Enter Year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is Leap Year")
else:
    print(year, "is NOT a Leap Year")

#3. Password Checking
a = input("Enter Password:")
b = "python123"

if a == b:
    print("Password Matched")
else:
    print("Invalid Password")