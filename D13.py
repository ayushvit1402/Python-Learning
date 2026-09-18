# '''
# 1.FizzBuzz Challenge
# '''
# n = int(input("Enter the no:"))

# for i in range(1, n+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i % 3 ==0:
#         print("Fizz")
#     elif i % 5 ==0:
#         print("Buzz")
#     else:
#         print(i) 

# '''
# 2.Count the Vowels
# '''
# s = input("Enter The String:").lower().strip()
# count = 0

# for i in s:
#     if i in "aeiou":
#         count+=1

# print(count)

# '''
# 3.Distinct and Sorted Elements
# '''
# n = list(map(int,input("Enter no.s:").split()))
# uni = []

# for i in n:
#     if i not in uni:
#         uni.append(i)

# uni.sort()
# print(*uni)

# '''
# 4.Student Average Score Update
# '''
# import statistics as stat

# n = input("Enter the Name:")
# m = list(map(int,input("Marks:").split()))
# t = tuple(m)

# dict = {}
# avg = stat.mean(m)
# d_avg = (f'{avg:.2f}')

# dict["Name"] = n
# dict["Scores"] = t
# dict["average"] = d_avg


# print(dict)

# print({1:"a",2:"b",3:"c"}[3])

t = (2,5,4,7,8,9)
a= sorted(t)
print(a)
    