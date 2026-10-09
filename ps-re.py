import re

re_string = "1/1/2022 12:04:54 MikeW login.aspx Successful login"
result_pattern = r"Success\w*"
date_pattern = r"\d+/\d+/\d+"

rpattern = re.compile(result_pattern)
dpattern = re.compile(date_pattern)


print("-----------------------------------------------------------")

res = rpattern.match(re_string)
dt =  dpattern.match(re_string)
print("[*]Match the pattern 'Success' followed by alphanumeric char(s)")
if res is not None:
    print(res.string)
    print(res.pos) 
    print(res.group()) 
else:
    print("None")

res = rpattern.search(re_string)
dt =  dpattern.search(re_string)
print("[*]Search the pattern 'Success' followed by alphanumeric char(s)")
print(res.string)
print("result: " + res.group())
print(res.start()) 
print("date: " + dt.group())  

"""

res = re.split(r"\s", re_string)
print("[*]Split up string by the whitespace and add each individual part to a list")
print("All tokens:", res)
print("Result token:", res[4])
print("Date token:", res[0])

print("-----------------------------------------------------------")

res = re.findall(r"\d", re_string)
print("[*]Print all the digits in a list")
print(res) 
"""