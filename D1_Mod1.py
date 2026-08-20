'''
EASY PROBLEMS
''' 
'''
1.Say "Hello, World! & Formatting
'''
name = input("Enter Your Name:")
age = int(input("Enter your Age:"))

print(f"Hello {name}, you will be {age+1} next year!")

'''
2.Typecasting & Arithmetic
'''
a = float(input("Enter first no:"))
b = float(input("Enter second no:"))

f_sum = a+b
i_sum = int(a+b)

print(f"Float Sum:{f_sum}")
print(f"Integer Sum:{i_sum}")


'''
3. Base Convertor (Binary to Decimal & Hex)
'''
bs = input("Enter Binary String:")
dv = int(bs, 2)
hd = hex(dv)
print(dv)
print(hd)

'''
MODERATE PROBLEMS
''' 
'''
4.Swap Without Third Variable
'''
a = input("First No:")
b = input("Second No:")

a,b = b,a

print(f"a = {a} \nb = {b}")

'''
5.Membership & Identity Checker
'''
s = input("Enter the Sentece: ")
w = input("Enter the word to be checked: ")

print(f"Contains word: {w in s}\nSame object: {s is w}")


'''
6. Bitwise Multiply & Divide by Power of 2
'''
n = int(input("Enter N: "))
k = int(input("Enter K: "))

ls = n<<k
rs = n>>k

print(f"Multiplied:{ls}\nDivided:{rs}")

'''
DIFFICULTPROBLEMS
''' 
'''
7.OPERATOR PRECEDENCE
'''
r = 2**3**2+10//3*4-5
print(f"Result: {r}")

