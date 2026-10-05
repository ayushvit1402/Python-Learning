# #1.
# '''
# Department Salary & Highest Earner
# '''
# def analyze_salaries(company_data):
#     nd =  {}
    
#     for d_n,l in company_data.items():
#         name = ""
#         h_s = 0
#         total_payout = 0

#         for e_n,m_s in l:
#             total_payout += m_s
#             if m_s > h_s:
#                 h_s=m_s
#                 name=e_n
        
#         nd[d_n]=(total_payout, name)
#     return nd

# c_d = {
#     "HR":[("Alice",40000),("Bob",50000)],
#     "Tech":[("Charlie",80000),("David",120000),("Eve",95000)]
# }

# print(analyze_salaries(c_d))

#2.
'''
Unique Tag Analyzer
'''
def get_unique_tags_by_autor(articles):

    dic = {}

    for a_n, t_s in articles:
        tags_list = t_s.split(",")
        
        if a_n not in dic:
            dic[a_n] = set()

        for tag in tags_list:
            dic[a_n].add(tag.strip().lower())

    result = {}
    for author, tags_set in dic.items():
        result[author]=len(tags_set)


    return result

art = [
    ("Rahul", "Python,AI,ML"),
    ("Sneha", "Web, HTML, CSS"),
    ("Rahul","python, Data Science, AI")
]

print(get_unique_tags_by_autor(art))




