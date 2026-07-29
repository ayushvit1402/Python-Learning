# WAP to ask to user to enter names of their 3 favourite movies & store them in a list 
mov = []
a = input("Name of fav movies1: ")
b = input("Name of fav movies2: ")
c = input("Name of fav movies3: ")

mov.append(a)
mov.append(b)
mov.append(c)
print(mov)

mov1 = []
mov1.append(input("enter mov 1:"))
mov1.append(input("enter mov 2:"))
mov1.append(input("enter mov 3:"))
# print(mov1)

#WAP to check if a list contains a palindrome of elements
list1 = ["a", "a", "b", "a", "b"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT Palindrome")

#WAP to count the number of students wuth the "A" grade in the following tuple.
grades = ("C", "D", "A","A","B","B","A")
print(grades.count("A"))

#Store the above values in a list & sort them from "A" to "D".
grades = ["C", "D", "A","A","B","B","A"]
grades.sort()
print(grades)