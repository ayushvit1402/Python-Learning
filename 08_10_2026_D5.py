#1
'''
Indian Mobile Number Validator
'''
import re

p_no = input("Enter Phone No:").strip()

pattern = r'^[6-9]{1}[0-9]{9}'

if re.match(pattern,p_no):
    print("True")
else:
    print("False")

#2
'''
Indian Postal PIN Code Checker
'''
import re

pin = input("Enter PIN:").strip()

pat = r'^[1-9]\d{5}$'

if re.match(pat,pin):
    print("True")
else:
    print("False")

#3
'''
VIT Student Email Address Filtering
'''
import re

e_m = input("Enter email:").strip()

pat = r'^[a-zA-Z0-9._]+@vitstudent\.ac\.in$'

if re.search(pat,e_m):
    print("True")
else:
    print("False")

#4
'''
VIT Course Code Validator
'''
import re

c_code = input("Enter Course Code:").strip()

pat = r'^[A-Z]{3}[0-9]{4}$'

if re.match(pat,c_code):
    print("True")
else:
    print("False")

#5
'''
TN Vehicle Number Plate Extractor
'''
import re

veh_no = input("Enter Text:").strip()

pat = r'\bTN[-]?\d{2}[-]?[A-Z]{1,2}[-]?\d{4}\b'

print(re.findall(pat,veh_no))

