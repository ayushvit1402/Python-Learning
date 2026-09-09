'''
1. Given an array of integers, find a contiguous non-empty subarray that has the largest product, and print
that maximum product
'''
n = int(input("Size of the array:"))
a = list(map(int,input("Input integers:").split()))[:n]

max_prod = a[0]

for i in range(n):          #starting point of subarray
    current_prod = 1
    for j in range(i,n):      #ending point of subarray 
        current_prod *= a[j]
        if current_prod > max_prod:
            max_prod = current_prod

print(max_prod)

'''
2.Reverse Digits and Check Palindrome
'''
n = int(input("No to be Checked:"))
b = str(n)

while True:
    if b == b[::-1]:
        print(int(b[::-1]))
        print("Palindrome")
    else:
        print(int(b[::-1]))
        print("NOT Palindrome")
    break

#Mathematical Approach (Using while Loop)
n = int(input())
og_n = n
rev_n = 0

while n > 0:
    dgt = n % 10    #Last Digit
    rev_n = rev_n*10 + dgt
    n = n//10       #Remove Last digit

print(rev_n)

if og_n == rev_n:
    print("Palindrome")
else:
    print("NOT Palindrome")

'''
3.Character Frequency & Grouping
'''
#Input Clean
s = input("Enter Sentence:")
s = s.lower() #lower all the chr in s

cln_str = ""    #Empty str having only alphabets
for char in s:
    if char.isalpha(): # .isaplha() check that whether char(our var) is alphabet or not
        cln_str += char    

#Frequency Count(Using dict)
freq_dict = {}

for char in cln_str:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

#Grouping the Frequency (Rev Dict Concept)
grp_dict = {}

for char, count in freq_dict.items():
    if count not in grp_dict:
        grp_dict[count] = []    #agar freq first time aayi h toh empty list bnao

    grp_dict[count].append(char)

for count in sorted(grp_dict.keys()):
    char_list = sorted(grp_dict[count])
    print(f"{count}: {char_list}")