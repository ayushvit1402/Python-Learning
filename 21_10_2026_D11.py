#1.Average Age and Older Count
def calculate_average_age(ages):
    avg = sum(ages)/len(ages)
    count_old = 0
    for age in ages:
        if age>avg:
            count_old+=1
    return round(avg,1),count_old

n = int(input())
l = []

for i in range(n):
    age = int(input())
    l.append(age)

average, old_count = calculate_average_age(l)
print(average)
print(old_count)

#2.Adjusted Fence Length Difference
def adjust_fence_length(a,b,c):
    lengths = [a,b,c]
    long_len = max(lengths)
    short_len = min(lengths)

    adj_long_len = long_len*0.9
    adj_short_len = short_len+5

    adj_tot_len_diff = (long_len-short_len)+(adj_long_len-adj_short_len)

    return round(adj_tot_len_diff,1)

a = float(input("Len of First Side:"))
b = float(input("Len of Second Side:"))
c = float(input("Len of Third Side:"))

print(adjust_fence_length(a,b,c))

#3.Reverse Sentence Words
def rev_sent(sentence):
    a = list(sentence.split())
    rev_l = a[::-1]

    a = " ".join(rev_l)
    return a

s = input("Enter The Sent to be rev:")
print("Reversed sentence:",rev_sent(s))

#4.Recursive Exponential Sum
def exponential_sum(x,n):
    if n == 0:
        return 0
    else:
        return x**n + exponential_sum(x,n-1)

x ,n = map(int,input("Enter Base and exp:").split())
print(exponential_sum(x,n))

#5.Final Project Score Calculation
def calculate_final_project_Score(c,cw,e,ew,p,pw):
    cs = c*cw
    es= e*ew
    ps = p*pw
    fin_Score = cs+es+ps

    return(round(fin_Score,1))

c = int(input())
e = int(input())
p = int(input())

cw = float(input())
ew = float(input())
pw = float(input())

print(f"Final Score: {calculate_final_project_Score(c,cw,e,ew,p,pw)}")

    
#6.Lambda with Filter (Positives) and Map (Squares)
n = int(input())
nums = list(map(int,input().split()))[:n]

pos = list(filter(lambda x:x>0,nums))
sqr = list(map(lambda x:x**2,pos))

print(f"Positives:{pos}")
print(f"Squares:{sqr}")

#7. Sort Words by Length
n = int(input())
l = []
for i in range(n):
    word = input().strip()
    l.append(word)
a = sorted(l,key=lambda x: len(x))
print(a)

#8.Simple Interest Lambda Function
s_i = lambda p,r,t:(p*r*t)/100

p = int(input())
r = int(input())
t = int(input())

print(f"Simple Interest: {s_i(p,r,t):.2f}")

#9.Separate Evens and Odds with Lambda
n = int(input())
nums = list(map(int,input().split()))[:n]

even = list(filter(lambda x:x%2 ==0,nums))
odd = list(filter(lambda x:x%2 ==1,nums))

print("Evens:",even)
print("Odds:",odd)

#10. Filter Scores Above Average
n = int(input())
scores = list(map(int,input().split()))
avg = sum(scores)/n
fil_lst = list(filter(lambda x: x>avg,scores))
print("Average:", round(avg,2))
print("Above Average:", fil_lst)

#11.Cart Item Limit Exception
class CartItemLimitException(Exception): pass
def validate(item_count):
    if item_count > 20:
        raise CartItemLimitException("Cart Item Limit: Cannot add more than 20 items")
    return item_count

item_count = int(input())
try:
    result = validate(item_count)
    print("Items in Cart:", result)
except CartItemLimitException as e:
    print(e)

#12.Too Many ATM PIN Attempts Exception
class TooManyAttemptsException(Exception): pass
def check_attempt(attempts):
    if attempts > 3:
        raise TooManyAttemptsException("Too Many Attempts: Account locked after 3 tries")
    return attempts

attempts = int(input())
try:
    res = check_attempt(attempts)
    print(f"Attempt Accepted:{attempts}")
except TooManyAttemptsException as e:
    print(e)

#13.Count Character Occurrences in File
def filename(lines,n,filename):
    with open(filename,"w+") as f:
        for i in range(n):
            f.write(lines[i]+"\n")

def countCharacterOccurences(filename,character):
    with open(filename,"r") as f:
        count = 0
        for char in f.read():
            if char.lower() == character.lower():
                count += 1
    return count

n = int(input())
lines_list = []
for i in range(n):
    s = input().strip()
    lines_list.append(s)
fname = "text.txt"
filename(lines_list,n,fname)

char = input().strip()
print(f"Occurrences of {char} : {countCharacterOccurences(fname,char)}")










     
    