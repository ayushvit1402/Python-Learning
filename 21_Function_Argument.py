def avg(a, b=1):   #a=required arg, b=Default arg
    print("The average is:",(a+b)/2)

# avg(4,6)
avg(a=5)

def average(*numbers):  #Variable Length Arg
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum+=i
    # print("Average is:",sum/len(numbers))
    return sum/len(numbers)

c = average(5,6,7,1)
print(c)

'''
-4 types of arguments
1.Default Arg
2.Keyword Arg
3.Variable Length Arg
4.Required Arg
'''
