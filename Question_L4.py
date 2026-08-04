#1. Store following word meanings in a python dictionary:
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "List of facts and figures"]


}
print(dict)

#2. You are given a list of students for students. assume one classroom is required for 1 subject. How many classrooms are needed by all students.
subject = {"python", "c++", "java", "python", "javascript","python","java","java","c++","c"}
print(len(subject))

'''
3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
Start with an empty dictionary & add one by one. Use suject name as key & mark as values
'''
marks = {}

phy = int(input("Enter Physics Marks: "))
chem = int(input("Enter Chem Marks: "))
maths = int(input("Enter maths Marks: "))


dict.update({"phy" : phy})
dict.update({"chem" : chem})
dict.update({"maths" : maths})

print(dict)

'''
4. Figure out a way to store 9 & 9.0 as a separate values in the set.
(You can take help of built-in data types)
'''
values = {9, "9.0"}
print(values)