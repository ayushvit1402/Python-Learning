# '''
# 1. Prime Checker & Factor List
# '''
# n = int(input("Enter the Number:"))


# if n == 1:
#     print("1 is neither prime nor composite.")

# n_prm = True

# for i in range(2,n):
#     if n%i == 0:
#         n_prm = False

# f_np = []
# f_p = []

# if n_prm == True and n > 1:
#     print("Number is Prime")
#     for a in range(1,(n+1)):
#         if n%a == 0:
#             f_p.append(a)
#     print(f"Factors:{f_p}")        

# elif n_prm == False:
#     print(f"{n} is NOT a Prime Number.")
#     for i in range(1,(n+1)):
#         if n%i == 0:
#             f_np.append(i)
#     print(f"Factors:{f_np}")

# '''or'''
# n = int(input("Enter the Number: "))

# if n == 1:
#     print("1 is neither prime nor composite.")
# else:
#     # 1. Factors nikalna (Sabhi numbers ke liye common)
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)

#     # 2. Prime Check Logic (Factors ki length se direct check kar sakte ho)
#     if len(factors) == 2:
#         print(f"{n} is a Prime Number!")
#     else:
#         print(f"{n} is NOT a Prime Number.")

#     print(f"Factors: {factors}")

# '''
# 2. Vowels & Consonants Counter
# '''
# s = input("Enter the sentence:").lower()

# vow = 0
# cons = 0
# for i in s:
#     if i.isalpha():
#         if i in "aeiou":
#             vow+=1
#         else:
#             cons+=1

# print(f"Vowels: {vow}")
# print(f"Consonants: {cons}")

'''
3.Remove Duplicates while Preserving Order
'''
n = list(map(int,input("Enter Numbers:").split()))
n_l = []

for i in n:
    if i not in n_l:
        n_l.append(i)

print(f"Original List:{n}")
print(f"Unique List:{n_l}")


