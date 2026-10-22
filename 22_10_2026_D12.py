# #1.Warehouse Barcode Symmetry
# def palindrome(s):
#     if len(s)<=1:
#         return "Palindrome"
#     if s[0]!=s[-1]:
#         return "Not Palindrome"
#     return palindrome(s[1:-1])

# wrd = input().strip()
# print(palindrome(wrd))

# #2.Escalator Step Combination 
# def febonaci(N):
#     if N <= 1:
#         return 1
#     return febonaci(N-1)+febonaci(N-2)

# n = int(input())
# print("Total No Of Ways:",febonaci(n))

# #3.Alternating Packet Validator
# def is_even_phase(n):
#     n = abs(n)
#     if n == 0:
#         return True
#     return is_odd_phase(n-1)

# def is_odd_phase(n):
#     n = abs(n)
#     if n == 1:
#         return True
#     return is_even_phase(n)

# n = int(input())
# if is_even_phase(n):
#     print("EVEN")
# else:
#     print("ODD")

# #4.Server Log Error Extractor
# wl = []
# with open("server.txt","r+") as f:
#     a = f.readlines()
#     for lno, reqline in enumerate(a,start=1):
#         if "ERROR" in reqline:
#             wl.append(f"{lno}."+" " + reqline)

# with open("error.txt","w+") as f:
#     f.writelines(wl)

# print(len(wl))

#5.Financial Ledger CSV Reconciler
with open("transaction.csv","r+") as f:
    a = f.readlines()
    b = []
    for i in a:
        lst = i.split(",")
    
    print(lst)
