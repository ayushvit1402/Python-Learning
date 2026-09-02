'''
1.
'''
name = input().lower()

s = []

for i in name:
    if i not in s:
        s.append(i)

if len(s) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")

'''
2.
'''
n = int(input()) #No of the prob
soln=0
for i in range(n): 
    a, b, c = map(int,input().split())
    if a+b+c>=2:
        soln=soln+1
print(soln)