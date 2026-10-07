#1
'''
Student Grade Performance Tracker
'''
def calculate_student_average(Student_Data):
    n_dict = {}

    for s_name, sub_mar in Student_Data.items():
        marks = []
        for sub,mar in sub_mar.items():
            marks.append(mar)
        avg = sum(marks)/len(marks)    
        n_dict[s_name] = round(avg,2)
    return n_dict

student_data = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Sneha": {"Math": 95, "Science": 92, "English": 96},
    "Aman": {"Math": 70, "Science": 65, "English": 72}
}

print(calculate_student_average(student_data))

#OR

def calculate_student_average(Student_Data):
    n_dict = {}
    
    for s_name, sub_mar in Student_Data.items():
        # Direct saare marks extract karein
        marks = sub_mar.values()
        
        # Average calculate karein
        avg = sum(marks) / len(marks)
        
        # String format ki jagah round() function use karein
        n_dict[s_name] = round(avg, 2)
        
    return n_dict

student_data = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Sneha": {"Math": 95, "Science": 92, "English": 96},
    "Aman": {"Math": 70, "Science": 65, "English": 72}
}

print(calculate_student_average(student_data))

#2
'''
E-Commerce Customer Order Summary
'''

def sum_electro_ord(orders):
    r_dic = {}

    for c_id,p_c,amt in orders:
        if p_c.lower() ==  "electronics":
            r_dic[c_id] = r_dic.get(c_id,0) + amt

    return r_dic

orders = [
    ("C101", "Electronics", 15000),
    ("C102", "Clothing", 2000),
    ("C101", "electronics", 5000),   # Total C101 Electronics = 20000
    ("C103", "Electronics", 8000)
]

print(sum_electro_ord(orders))

#3
'''
Word Frequency Counter
'''
def count_word_frequency(txt):
    words = txt.lower().split()

    dic = {}
    for i in words:
        dic[i]=dic.get(i,0)+1

    return dic

a = "Python is easy and python is powerful"
print(count_word_frequency(a))



