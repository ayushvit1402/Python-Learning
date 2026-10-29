import re
#1. Corporate Email Extractor
def extract_corporate_emails(text):
    pattern = r"\w*@techcorp.com"
    a = re.findall(pattern,text)
    b = sorted(a)
    return b

email = "Contact support@techcorp.com or admin123@techcorp.com. Also check external@gmail.com."
print(extract_corporate_emails(email))

#2.Indian Mobile Number Validator (Easy)
def validate_indian_numbers(numbers_list):
    val_no = []
    pat = r'(?:\+?91[\-\s]?)?([6-9]{1}[0-9]{9})'
    for num in numbers_list:
        a = re.match(pat,num)
        if a:
            val_no.append(a.group(1))
    return val_no

numbers = ["+91-9876543210", "91 9876543210", "0123456789", "987654321", "7890123456"]
print(validate_indian_numbers(numbers))

#3.URL Extractor from Web Logs (Easy)
def extract_urls(log_string):
    pat = r'https?://[\w\-\.:\/?=&%]+'
    a = re.findall(pat,log_string)
    return a

logs = "User visited https://www.google.com and then checked http://example.org/path?id=12 for updates."
print(extract_urls(logs))

#4.Social Media Hashtag & Mention Extractor (Easy)
def extract_tags_and_mentions(post):
    pat_hash = r'(#[\w\_]+)'
    pat_ment = r'(@[\w\_]+)'

    d = {}
    
    search_h = re.findall(pat_hash,post)
    search_m = re.findall(pat_ment,post)
    d["hashtags"] =search_h
    d["mentions"] =search_m
    return d

post_text = "Loving the new #Python release! Great job @python_dev and @guido for #Pythonlang."
print(extract_tags_and_mentions(post_text))


