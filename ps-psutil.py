import os
import psutil
"""
#print("NETWORK:\n", psutil.net_connections(kind='inet4')[0], "\n")
#print("USERS:\n", psutil.users(), "\n")
#print("PIDs:\n", psutil.pids(), "\n")

for proc in psutil.process_iter(['pid', 'name', 'username']):
   print(proc.info)


#p = psutil.Process()
p = psutil.Process(pid=1948)
with p.oneshot():
    print("\nName: " + str(p.name()))
    print("CPU Time: " + str(p.cpu_times()))
    print("CPU %: " + str(p.cpu_percent()))
    print("Create Time: " + str(p.create_time()))
    print("PPID: " + str(p.ppid()))
    print("Status: " + str(p.status()))



print("CPU times:", psutil.cpu_times())
print("CPU in use:", psutil.cpu_percent(interval=.1), "%")
print("Memory in use:", psutil.virtual_memory().percent, "%")
print("Disk usage", psutil.disk_usage('/').percent, "%")
print("Memory free:", psutil.virtual_memory().available/(1024**3), "GB")
print("Disk usage", psutil.disk_usage('/').free/(1024**3), "GB")
print(psutil.disk_partitions())
print(psutil.users())
print(psutil.boot_time())


"""
def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls

print(find_procs_by_name("winlogon.exe"))

