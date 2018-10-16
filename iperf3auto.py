def iperf():
    def custom_ssh_client(hostname,port=22,user=None,passwd=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,user,passwd)
        stdin,stdout,stderr=ssh.exec_command('killall -9 firefox-esr')
        ssh.close()

    details = custom_ssh_client('172.16.2.183',user='user',passwd='user')
    #p1 = subprocess.Popen(['iperf3', '-c', '10.10.10.30','-t300','-F' ,'manish_home.tar.xz'])
    #sleep(200)
    #i = +i
