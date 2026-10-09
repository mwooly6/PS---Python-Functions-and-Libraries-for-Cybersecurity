import sys

#sys.stderr = open('out-err.log', 'w')
#sys.stdout = open('out.log', 'w')

sys.stdout.write("Print Out - STDOUT 1\n")
sys.stderr.write("ERROR: fatal error - STDERR 1\n")

sys.stdout.write("Print Out - STDOUT 2\n")
sys.stderr.write("ERROR: fatal error - STDERR 2\n")

sys.stdout.write("Print Out - STDOUT 3\n")
sys.stderr.write("ERROR: fatal error - STDERR 3\n")

#uname = input("Enter Name: ")
#print("Hello " + uname)

#print("Argument:", sys.argv[1])

#print("\nPath:", sys.path[0])
#print("\nFull Path:", sys.path)
#print("\nVersion:", sys.version)
#print("\nVersion_Info:", sys.version_info)