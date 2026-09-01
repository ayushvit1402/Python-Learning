'''
1.Replace the element at a given 0-based index in a tuple with a new value and 
print the updated tuple
'''
n = list(map(int,input().split()))
idx = int(input())
nv = int(input())

n[idx] = nv

t = tuple(map(str,n))
print(t)

'''
2.  Find unique common elements between two tuples in the order of their first appearanc in the first tuple.
'''
n = int(input())
t1 = list(map(int,input().split()))

m = int(input())
t2 = list(map(int,input().split()))

c_id = []

for i in t1:
    for j in t2:
        if i == j:
            c_id.append(i)
            
u_id = []

for item in c_id:
    if item not in u_id:
        u_id.append(item)
        
t = tuple(u_id)
        
print(t)

'''
3. Given Student name and their ages, find and print the names od the oldest student.
'''
n = int(input())

name = []
age = []

for i in range(n):
    a = input()
    b = int(input())
    name.append(a)
    age.append(b)

oldest = max(age)
idx = age.index(oldest)

print(f"The oldest student is {name[idx]}")

'''
4. Check if a given color exists in a tuple of comma-separated colours
'''
a = tuple(input().split(","))
b = input()

clr = []

for colour in a:
    if colour == b:
        clr.append(b)
    

if b in clr:
    print(f"The color '{b}' is in the tuple.")
else:
    print(f"The color '{b}' is not in the tuple.")
      