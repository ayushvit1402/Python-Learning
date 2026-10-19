#lambda function
# filter()

'''
1.Check Wheather a word is Palindrome 
'''
words = ["madam","hello","level","python","radar"]
print(list(filter(lambda word:word == word[::-1],words)))

'''
2.Count the Vowels in each word
'''
words = ["apple","education","python","orange"]
for word in words:
    vowels = list(filter(lambda ch: ch.lower() in "aeiou",word))
    print(word, ":", len(vowels))


'''
3.Check whether a word start with 'Z'
'''
words = ["Zebra","apple","Zoo","orange","Zero","cat"]
result = list(filter(lambda word:word.lower().startswith("z"),words))
print(result)

'''
4.Check Pass or fail and count the students
'''
marks = [85,45,67,30,50,90,42,75]
#pass marks < 50
passed = list(filter(lambda mar:mar>50,marks))
failed = list(filter(lambda mar:mar<=50,marks))

print(f"{len(passed)} students are passed with Pass marks {passed}")
print(f"{len(failed)} students are passed with Pass marks {failed}")

#map()
'''
1.Finding Squares
'''
nums = [1,2,3,4,5]
#Normal Function
def sq(n):
    return n**2

squares = list(map(sq,nums))
print(squares)

#lambda Function
sq = list(map(lambda x:x**2,nums))
print(sq)

'''
2.Multiple lists
'''
a=[1,2,3]
b=[4,5,6]

sums=map(lambda x,y:x+y,a,b)
print(list(sums))

'''
3.Remainder Checker
'''
lst=[2,3,4,5,6,7,8,9,10]
rem=map(lambda x:x%2,lst)
print(list(rem))

'''
4.Check Pass and fail
'''
marks = [85,45,67,30,50,90,42,75]

result = list(map(lambda mark: "Pass" if mark>50 else "Fail",marks))
print(result)
print(f"Passed: {result.count("Pass")}\nFailed: {result.count("Fail")}")

'''
5.Calculate the Sum of Absolute Value
'''
nums = [-10,20,-30,40,-50]
result=list(map(abs,nums))
print(result)
print(sum(result))