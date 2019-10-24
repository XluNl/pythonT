
import subprocess
# a = subprocess.Popen('dir',shell=True)
a = subprocess.Popen('ipconfig',shell=True,stdout=subprocess.PIPE)
data = str(a.stdout.read(),'gbk')
print(bytes(len(str(data))))
print(data)