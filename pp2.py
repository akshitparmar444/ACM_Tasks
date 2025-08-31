import re

def transform_text(input_text: str) -> str:
    l={}
    name = re.search(r"Name:\s*([A-Za-z]+)", input_text)
    if name:
        l["Name"] = name.group(1)
    email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", input_text)
    if email:
        l["Email"] = email.group(0)
    date = re.search(r"\d{4}-\d{2}-\d{2}", input_text)
    if date:
        l["Date"] = date.group(0)
    return l

str="My Name: Akshit .My email is parmarakshit77@gmail.com.Todays date is 2025-08-31"
str1='''Hello Team,  

This is to inform you that our new member has joined the research club.  
My Name: Akshit Parmar, and I am excited to collaborate with everyone.  
You can always reach me at parmarakshit77@gmail.com for queies.  

The official joining Date: 2025-08-31.  
I look forward to working on AI, data science, and research activities with all of you.  

Regards,  
Akshit  

'''

print(transform_text(str1))