import sys
import os


#os.system("ping 127.0.0.1")
#os.system("ping " + sys.argv[1])

#with open(os.path.join(sys.path[0], "log.txt"), "r") as f:
#  sys.stdout.write(f.read())

#os.remove("temp.txt")

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
     print(os.path.join(root, name))