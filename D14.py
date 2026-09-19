# '''
# 1.Common Values Between Two Tuples
# '''
# t1 = eval(input("First Tuple:"))
# t2 = eval(input("Second Tuple:"))

# l = [x for x in t1 if x in t2]
# l.sort()

# t3 = tuple(l)

# print(t3)

# '''
# 2.Uniuque Elements Preserving Order
# '''
# l1 = eval(input())

# a = list(dict.fromkeys(l1))
# print(a)

# '''
# 3.Merge Dictionaries with Evaluated Inputs
# '''
# d1 = eval(input())
# d2 = eval(input())

# d3 = d1.copy()

# for key, value in d2.items():
#     if key in d3:
#         d3[key] += value
#     else:
#         d3[key] = value
    
# print(d3)

# '''
# 4. Frequency Map From Evaluated List
# '''
# l = eval(input())
# d = {}

# for i in l:
#     d[i] = l.count(i)

# print(d)

# '''
# 5. Filter Tuple Items by Threshold
# '''
# l = eval(input())
# thr = int(input())

# l1 = []

# for stu, marks in l:
#     if marks >= thr:
#       l1.append(stu)

# print(l1)  

'''
6. Dictionary Key Inversion with Lists
'''
d = eval(input())
d1 = {}

for k,v in d.items():
    if v not in d1:
        d1[v] = [k]
    else:
        d1[v].append(k)

print(d1)