import subprocess

#subprocess.run("dir", shell=True)
#subprocess.call("dir", shell=True)
#subprocess.check_call("dir", shell=True)
#subprocess.Popen("dir", shell=True)

#subprocess.run('c:\program files\OWASP\Zed Attack Proxy\zap.exe -quickurl http://www.example.com')
#subprocess.run('notepad.exe')
subprocess.check_output(["c:\program files\OWASP\Zed Attack Proxy\zap.exe", "-quickurl", "http://www.example.com"])

print("Finished")