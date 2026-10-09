#1
'''
Multi-Format Indian Phone Number Validator
'''
import re
p_n = input("Enter Phone no:").strip()

pat = r'^([6-9]\d{9})|(\+91[ -]?[6-9]\d{9})|(0[6-9]\d{9})$'

if re.match(pat,p_n):
    print("True")
else:
    print("False")

#2
'''
Strict International/Custom Domain Email Extractor
'''
import re
p_n = input("Enter email:").strip()

pat = r'\b[a-zA-Z0-9._-]+@[A-Za-z0-9.]+\.[a-zA-Z]{2,6}\b'

print(re.findall(pat,p_n))

#3
'''
Masking Sensitive Phone Numbers
'''
import re
p_n = input("Enter:").strip()

pat = r'\b[6-9]\d{5}(\d{4})\b'
repl = r"XXXXXX\g<1>"

a = re.sub(pat,repl,p_n)
print(a)
