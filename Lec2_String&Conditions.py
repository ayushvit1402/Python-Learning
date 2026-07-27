#STRINGS
str1="This is a string.\nwe are creating it in python."
print(str1)

str1="Ayush"
len1= len(str1) #Length of the string
print(len1)
str2="Mishra"
len2=len(str2)
print(len2)
final_str=str1+" "+str2 #Cancatenation 
print(final_str)
len3=len(final_str)
print(len3)

## indexing
str= "apna college"
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

str="apple"
print(str[-5:-2])

##  Slicing
str = "I am a very good boy"
print(str[0:4])

##String Functions
str= "i am from studying python from ApnaCollege"
str1 = str.count("from")
str2 = str.endswith("ege")
str3 = str.capitalize()
str4 = str.replace("python","Java")
str5 = str.find("from")

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

#CONDITIONAL STATEMENTS
light = "orange"
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "orange"):
    print("Wait")
else:
    print("Light is broken")

print("End of Code")

num =  5
if(num > 2):
    print("Greater than 2")
elif(num > 3):
    print("Greater than 3")

age = 11
if(age >= 18):
    print("Can Vote") #indentation
else:
    print("Can't Vote")

m = int(input("Enter student Marks: "))
if(m >= 90 ):
    Grade = "A"
elif(m >= 80 and m < 90):
    Grade = "B"
elif(m >= 70 and m < 80):
    Grade = "C"
else:
    Grade= "D"

print(Grade)

#Nesting
age = int(input("Enter your Age: "))

if(age >= 18):
    if(age >= 80):
        print("Cannot Drive")
    else:
        print("can drive")
else:
    print("cannot drive")