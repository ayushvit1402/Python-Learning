# #1
# '''
# VIT Student Grade Point Evaluator
# '''
# def calculate_gpa(grades_dict):
#     point = 0.0
    
#     for cour, grd in grades_dict.items():
        
#         if grd == "S":
#             point += 10
#         elif grd == "A":
#             point += 9
#         elif grd == "B":
#             point += 8
#         elif grd == "C":
#             point += 7
#         elif grd == "D":
#             point += 6
#         elif grd == "E":
#             point += 5
#         elif grd == "F":
#             point += 0
#     gpa = point/len(grades_dict.keys())
#     r_gpa = f'{gpa:.2f}'
#     return r_gpa

# dict_s = {"CSE1001": "S", "MAT2002": "A", "PHY1001": "B"}
# print(calculate_gpa(dict_s))

#2
'''
Unique Attendence & Regular Student.
'''
def check_attendance(attendance_records):
    if not attendance_records:
        return []

    com_stud = set.intersection(*map(set, attendance_records))
        
    return sorted(list(com_stud))    

lst = [
    ["22BCE101", "22BCE102", "22BCE103"],
    ["22BCE101", "22BCE103"],
    ["22BCE101", "22BCE102", "22BCE103"]
]

print(check_attendance(lst))
