'''
1. Write a Python program that takes an integer
from the user and determines whether it is an
even number or an odd number.
'''
n =int(input("Enter no:"))

if n%2 == 0:
    print("EVEN")
else:
    print("ODD")

'''
2. Write a Python program that accepts N
numbers from the user and determines whether
each number is even or odd.
'''
N = int(input("Enter how many numbers you want to Check:"))

for i in range(N):
    num = int(input(f"Enter number {i+1}:"))
    if num%2 == 0:
        print(f"{num} is a EVEN no.")
    else:
        print(f"{num} is a ODD no.")


'''
3. Print all the factors of a given number.
'''

n = int(input("Given No:"))

for i in range(1,n+1):
    if n%i == 0:
        print(i, end=" ")

