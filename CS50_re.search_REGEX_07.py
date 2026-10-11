email = input("What's your email?").strip()

#1
if "@" in email:
    print("Valid")
else:
    print("Invalid")

#2
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

#3
username, domain = email.split("@")

if (username) and ("." in domain):
    print("Valid")
else:
    print("Invalid")

#4
username, domain = email.split("@")

if (username) and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

import re

email = input("What's your email?").strip()
#5
# re.search(pattern,string, flags = 0)

if re.search("@",email):
    print("Valid")
else:
    print("Invalid")

#6
if re.search(".*@.*",email):
    print("Valid")
else:
    print("Invalid")

#7
if re.search(".+@.+",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#8
#intro of escape seq \
# r"...." - raw string so that python do not treat \ as usual

if re.search(r".+@.+\.edu",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#9
#intro to startswith (^) and endswith($)

if re.search(r"^.+@.+\.edu$",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#10
#intro to [] for set of character and [^] and its complementation

if re.search(r"^[^@]+@[^@]+\.edu$",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#11
if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9]+\.edu$",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#12
#intro of () and | - or
if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9]+\.(edu|com|gov|net)$",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#13
# \w - word character

if re.search(r"^\w+@\w+\.edu$",email):    #..* ==.+
    print("Valid")
else:
    print("Invalid")


#14
# intro of flags (3rd arguement "re.IGNORECASE") 

if re.search(r"^\w+@\w+\.edu$",email, re.IGNORECASE):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#15
# intro of flags (3rd arguement "re.IGNORECASE") 
email - malan@cs50.harvard.edu

if re.search(r"^\w+@(\w+\.\w+|\w+)\.edu$",email, re.IGNORECASE):    #..* ==.+
    print("Valid")
else:
    print("Invalid")

#16
if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE):    #..* ==.+
    print("Valid")
else:
    print("Invalid")






'''
. any chacter except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetitions
{m} m repetitions
{m-n} m-n repetitions

^ matches the start of the string
$ matches the end of the string or just before the newline at the end of the string
[] set of characters
[^] complementing the set

\d decimal digit
\D not a decimal digit
\s whitespace character
\S not a whitespace Character
\w word character..... as well as numbers and the score
\W not a word character

A|B either A or B
(...) a group
(?:...) non-capturing version

re.IGNORECASE
re.MULTILINE
re.DOTALL



'''
