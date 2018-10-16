from subprocess import Popen 

p1 = Popen(['ifconfig', 'eth0', '198.168.1.13','up'])
p2 = Popen(['ifconfig', 'wlan0', '172.168.1.25','up'])
