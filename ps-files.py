f = open("temp.txt", "w")
f.write("I wrote this text\n")
f.write("I wrote more text ")

#with open("temp.txt", "a") as f:
#   f.write("I appended this text\n")

f = open("temp.txt", "r")
print(f.read())