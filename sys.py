import os,time
import subprocess
a=os.system("ls")
p3 = subprocess.Popen(['ps'])
print(a,p3)
time.sleep(10)
p3.kill()

