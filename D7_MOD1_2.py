'''
1.Reverse Words in a sentence.
'''
s = input("Enter Sentence:").split()
l = []
for i in range((len(s)+1)):
    if i != 0:
        e = s[-i]
        l.append(e)

print(*l)

'''or'''
s = input("Enter Sentence: ").split()
reversed_words = s[::-1]
print(" ".join(reversed_words))

'''or'''
s = input("Enter Sentence: ").split()
print(" ".join(reversed(s)))

'''
Simple Calculator with Loop
'''
while True:
    a = int(input("First No:"))
    b = int(input("Second No:"))
    c= input("Choose Operator(+,-,*,/):")

    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        if b != 0:
            print(a/b)
        else:
            print("Cannot divide by zero!").lower()
    else:
        print("Invalid Operator")

    q = input("Do you want to continue?")

    if q != "yes":
        print("Program Ended!")
        break
