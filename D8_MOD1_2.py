'''
1.Palindrome Number Checker
'''
num = int(input("Enter the no:"))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = (rev*10) + digit
    temp = temp // 10

if num == rev:
    print(f"{num} is a Palindrome Number.")
else:
    print(f"{num} is NOT a Palindrome Number.")