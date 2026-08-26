# '''
# 1.Word Count & Longest Word Finder
# '''
# n = input("Enter Sentence:").split()
# print(f"Total Words: {len(n)}")

# l = []
# for a in n:
#     s = len(a)
#     l.append(s)

# l.sort() 
# b = l[-1]

# for i in n:
#     if len(i) == b:
#         print(f"Longest Word: {i} with Length:{len(i)}")

# '''or'''

# w = input("Enter Sentence:").split()
# long_w = max(w, key=len)
# print(f"Total Words: {len(w)}")
# print(f"Longest Word:{long_w} with Length: {len(long_w)}")

'''
2. Number Frequency Counter
'''
n = list(map(int, input("Enter NO.:").split()))
t = int(input("Enter target no:"))

l = []
ind = []
for i in n:
    if i == t:
        l.append(i)
for j in n:
        if j == t:
             ind.append(l.index(j))

print(f"{t} appeared {len(l)} times.")
print(f"Found at indices: {ind}")