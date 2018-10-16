import paramiko

def custom_ssh_client(hostname,port=22,user=None,passwd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,user,passwd)
    stdin,stdout,stderr=ssh.exec_command('ps') #Execute the ls command
    #stdout will store the output for the command
    #stderr will store the errors and returns it if araises.
    #return stdout.read()
    ssh.close()

details = custom_ssh_client('172.16.2.183',user='user',passwd='user')
#Enter your IP_Address, Username and Password in the above function.
print(details)
