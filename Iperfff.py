import paramiko
import subprocess
from time import sleep
i = 1
for i in range (3):
    def custom_ssh_client(hostname,port=22,user=None,passwd=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,user,passwd)
        stdin,stdout,stderr=ssh.exec_command('iperf3 -s -1 -i 1 >> A.txt')
        ssh.close()

    details = custom_ssh_client('10.10.10.30',user='user',passwd='user')
    p1 = subprocess.Popen(['iperf3', '-c', '10.10.10.30','-t300','-F' ,'manish_home.tar.xz'])
    sleep(200)
    i = +i
