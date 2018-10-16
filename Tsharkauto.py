from subprocess import Popen
from time import sleep
p1 = Popen(['iw', 'phy','phy0', 'interface','add','mon0','type','monitor'])
p2 = Popen(['ifconfig', 'mon0','up'])
p3 = Popen(['tshark','-i','mon0','-wcoch.pcap'])
sleep(30)
p3.kill()
