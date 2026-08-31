'''
1. Find the most frequent word in input text.
If count match, pick the word that appeared first.
'''
a = input()

clr_txt = ""


for i in a:
        if i.isalpha() or i == " ":
            clr_txt += i
        else:
            clr_txt += " "

words = clr_txt.split()

max_count = 0
b_wrd = ""

for word in words:
    cnt = words.count(word)
    if cnt > max_count:
        max_count = cnt
        b_wrd = word
    
print(f"The most frequent word is '{b_wrd}' with a count of {max_count}")

'''
2.Extract even numbers from input integers and output as a tuple.
'''
n = list(map(int,input().split()))

l = []

for i in n:
    if i % 2 ==0:
        l.append(i)

t = tuple(l)

print("New Tuple with Even Integers:")
print(t)

'''
3. Take 'n' integers into a list, convert to tuple, print tuple and concatenate elements without spaces.
'''
n =  int(input())

lst = []

for i in range(n):
    elm = int(input())
    lst.append(elm)
    
t = tuple(lst)
print(t)
print("".join(map(str,t)))

'''
3. Take comma-separated integers, convert to a tuple, and print its length.
'''
n = tuple(map(int,input().split(",")))
print(len(n))