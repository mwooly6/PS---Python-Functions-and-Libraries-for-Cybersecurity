"""
STR = " PYTHON "
print(">" + STR + "<")
STR = STR.strip()
print(">" + STR + "<")

STR = " PYTHON "
print(">" + STR[1:7] + "<")

"""
LOG_FILE = "2022/01/01 04:12:05 MikeW 200 success login.aspx"
PARTS = LOG_FILE.split()

Date = PARTS[0]
Time = PARTS[1]
User = PARTS[2]
Status = PARTS[3]
Result = PARTS[4]
Page = PARTS[5]

New_Date = Date[5:] + "/" + Date[:4]

print("On {}, User {} had {} on page: {}".format(New_Date, User, Result, Page))