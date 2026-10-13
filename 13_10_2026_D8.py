#1
'''
Smart Note-Saver App
'''
f = open("my_notes.txt","w")
f.write("First note: Learning Python file handling.")
f.close()

p = open("my_notes.txt","a+")
p.write("\nSecond note: Practicing in VS Code.")
p.seek(0)
print(p.read())
p.close()

#or 

f = open("my_notes.txt","w")
f.write("First note: Learning Python file handling.")
f.close()

a = open("my_notes.txt","a")
a.write("\nSecond note: Practicing in VS Code.")
a.close()

r = open("my_notes.txt","r")
print(r.read())
r.close()

#2
'''
Student Report Card & Cursor Magic
'''
f = open("report.txt","w+")
f.write("Alice: 85\nBob: 90\nCharlie: 95\n")
f.seek(0)
print(f.read())
f.close()

#3
'''
VIT Exam Hall Seating Allocator
'''
def group_students_by_branch(reg_list):

    dic = {}
    for reg in reg_list:
        branch = reg[2:5]
        if branch not in dic:
            dic[branch]=[]
        dic[branch].append(reg)
    return dic

lst = ['22BCE1023', '21BME0412', '22BCE5012', '23CSE1005', '21BME9999']
print(group_students_by_branch(lst))