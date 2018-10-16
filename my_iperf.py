import subprocess
from time import sleep
# Ask the user for input
# host = raw_input("Enter a host to ping: ")	

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['iperf3', '-c', '172.16.2.135','-F' ,'Result.txt'])#, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#sleep(10)
#out, err = p1.communicate()
print '================='
#print out
print '================='
#p1.kill()
#p1 = subprocess.Popen(['killall', '-9','iperf3'], stdout=subprocess.PIPE)


# Run the command
#output = p1.communicate()[0]

#print output
