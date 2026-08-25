# """
# 1. Reverse String & Palindrome Check
# """
# a = input("Enter Word:")
# a = a.lower()
# b = a[::-1]

# if a == b:
#     print("PALINDROME")
# else:
#     print("Not PALINDROME") 

# """
# 2. Dynamic Password Strength Validator
# """
# a = input("Enter Password:")

# # Flags
# h_d = False
# h_u = False

# for i in a:
#     if i.isdigit():
#         h_d = True
#     elif i.isupper():
#         h_u = True

# if len(a) < 8:
#     print(f"Password is two short atleast {8-len(a)} more character is required.")
# elif not h_d:
#     print("Weak Password: at least ONE DIGIT is required")
# elif not h_u:
#     print("Weak Password: at least ONE UPPER CASE is required")
# else:
#     print("Status: Strong Password!")

"""
3. Number Pattern & Digit Sum
"""
n = input("Enter No:")
sum = 0

for i in n:
    sum += int(i)

print(f"Total Sum:{sum}")

print("Pattern:")
for a in range(1,len(n)+1):
    print("*"*a)
