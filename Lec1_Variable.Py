#arithmetic operators
a=5
b=2
sum=a+b
diff=a-b
prod=a*b
div=a/b
print(sum)
print(diff)
print(prod)
print(div) #always get a floating value 
print(a%b) #remainder when a get divided by b
print(a**b) #a^b

#relational operators
a=50
b=20
print(a == b) #is a equal to b
print(a != b ) #is a not equal to b
print(a >=b) #is a greater than or equal to b
print(a<=b) #is a less than or equal to b
print(a>b) #is a greater than b
print(a<b) #is a less than b

#assignment operator
num = 10
# num += 10
# num -= 10
# num *= 10
# num /= 10
# num %= 10 
num **=5
print("num :", num)

#Logical Operators
a=50
b=30
print(not (a>b))

val1=False
val2=False
print("AND operator:", val1 and val2)
print("OR operator:", (a==b) or (a>b))

#type conversion
a="2"
b=4.25

print(type(a))

#type casting
a=1
b="2"
c=int(b)
print(a+c)

a=3.14
a=str(a)
print(type(a))

#input in python
name=input("Enter your name: ")
print("Welcome ",name)

val=int(input("enter the value:"))
print(type(val))

