#re.match(pattern,string,flags=0) :match the start only
#re.fullmatch(pattern,string,flags=0) :match both start and end

name = input("What's your name?").strip()

#1
if "," in name:
    last,first = name.split(", ")
    name = f"{first} {last}"
    
print(f"Hello, {name}")

#2

import re

name = input("What's your name?").strip()
matches = re.search(r"^(.+), (.+)$",name)

if matches:
    name = matches.group(2) +" "+matches.group(1)
print(f"hello, {name}")

#3
#name = Malan,    David
name = input("What's your name?").strip()
matches = re.search(r"^(.+), ?(.+)$",name)

if matches:
    name = matches.group(2) +" "+matches.group(1)
print(f"hello, {name}")

#4
name = input("What's your name?").strip()
matches = re.search(r"^(.+), *(.+)$",name)

if matches:
    name = matches.group(2) +" "+matches.group(1)
print(f"hello, {name}")

'''
Walrus Operator 
:=
'''
name = input("What's your name?").strip()

if matches := re.search(r"^(.+), *(.+)$",name):
    name = matches.group(2) +" "+matches.group(1)
print(f"hello, {name}")


#Twitter

url = input("URL: ").strip()

#1
username = url.replace("https://twitter.com/","")
print(f"Username: {username}")

#2
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

#3
#re.sub(pattern,repl,string,count=0,flags=0)
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(wwww\.)?twitter\.com/","",url)
print(f"Username: {username}")

#4
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE)

if matches:
    print(f"Username:",matches.group(2))

#5
#using walrus operator

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username:",matches.group(2))

#6
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username:",matches.group(1))

#7
#intro to 
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$",url, re.IGNORECASE):
    print(f"Username:",matches.group(1))