#List
marks = [94.4, 87.5, 95.2, 65.2, 45.1]
print(len(marks))
print(marks[0])
print(marks[1])

# It can store elements of different types
# eg. integers, float, string, etc..
student = ["Karan", 95.4, "Delhi"]
print(student)

#string- immutable
#lists- mutable 
student = ["Karan", 95.4, "Delhi"]
str = "hello"
print(str[0])
print(student[0])
student[0] = "arjun"
print(student)

#LIST SLICING
marks = [87, 64, 33, 95, 76]
print(marks[ : 4])
print(marks[-3 : -1])

#LIST METHODS 
list = [2, 1, 3]
list.append(4) #adds one element at the end [2, 1, 3, 4]
print(list)

list.sort() #sorts in ascending order [1, 2, 3, 4]
print(list)

list.sort(reverse = True) #sorts in descending order [4, 3, 2, 1]
print(list)

list.reverse() #reverse the list [1, 2, 3, 4]
print(list)

list.insert(1, 5) #insert element at index
print(list)

list1 = [1, 2, 1, 3]
list1.remove(1) #remove the first occurrence of element [2, 1, 3]
print(list1)
list1.pop(1) #removes element at idx
print(list1)

#TUPLES
tup = (2, 1, 3, 1)
print(tup[0])

tup = (1, 2, 3, 4 )
print(tup)
print(type(tup))
print(tup[1:3])

tup = (2, 1, 3, 4, 1, 2, 4)
print(tup.index(3)) #returns index of first occurrence tup.index(1) is 1

print(tup.count(2))