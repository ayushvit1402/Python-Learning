#1
'''
Library Book Fine and Late Return Tracker
'''

def calculate_library_fines(records):
    dic = {}

    for mem,b_tit, day_l in records:
        t_famt = 0
        if day_l <= 5:
            t_famt = 10*day_l
        else:
            t_famt = 50+(day_l-5)*20

        if mem not in dic:
            dic[mem] = t_famt
        else:
            dic[mem] += t_famt
        
    return dic

rec = [
    ("M101", "Python Guide", 3),
    ("M102", "Data Science", 7),
    ("M101", "SQL Basics", 6)
]

print(calculate_library_fines(rec))

#2.
'''
Unique Course Enrollment Analyzer
'''
def analyze_enrollments(enr):
    dic = {}

    for s_name,cat in enr:
        categories = cat.split(",")
        
        if s_name not in dic:
            dic[s_name] = set()

        for c in categories:
            dic[s_name].add(c.strip().lower()) 
    
    result = {}
    for student, cat_set in dic.items():
        result[student] = len(cat_set)

    return result

enrol = [
    ("Aman", "Coding,AI,ML"),
    ("Riya", "Coding,AI,ML"),
    ("Aman", "coding, Web Dev, AI")
]

print(analyze_enrollments(enrol))

#3.
'''
Supermarket Store Highest Profit Product
'''
def find_highest_profit_product(inventory):
    
    pro = ""
    m_t_p = 0
    for pro_n,info in inventory.items():
        c_p,s_p,u_S = info
        t_p = (s_p-c_p)*u_S
       
        
        if m_t_p<t_p:
            m_t_p = t_p
            pro=pro_n

    
    return (pro,m_t_p)

invent = {
    "Pen": (5,10,100),
    "Notebook": (30,50,40),
    "Eraser": (2,5,50)
}

print(find_highest_profit_product(invent))

