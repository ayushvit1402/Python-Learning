#Dictionary in Python
#Dictionaries are used to store data values in key:value pairs
#they are unordered, mutable and don't allow duplicate keys


info = {
    "name" : "ayush",
    "learning" : "coding",
    "Subjects" : ["Python", "Java", "C"],
    "topic" : ("dict", "sets"),
    "age" : 35,
    "is_adult" : True,
}
info["name"] = 23 #overwrite
info["Surname"] = "mishra"

print(info["name"])
print(info["learning"])
print(info["Subjects"])
print(info["topic"])
print(info["age"])


null_dict = {}
null_dict["name"] = "ayush mishra"
print(null_dict)

#Nested Dictionaries
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 95
    }
}
print(list(student.keys())) #type cast to list
print(len(student))
print(list(student.values()))
print(list(student.items()))
print(student["name2"]) #error
print(student.get("name2")) #None
new_dict = {"city" : "delhi"}
student.update(new_dict)
print(student)
print(student["subjects"]["chem"])

