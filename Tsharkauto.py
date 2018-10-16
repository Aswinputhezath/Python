from subprocess import Popen
from time import sleep
p1 = Popen(['iw'\t 'phy'\t'phy0'\t 'interface'\t'add'\t'mon0'\t'type'\t'monitor'])
p2 = Popen(['ifconfig', 'mon0','up'])
p3 = Popen(['tshark','-i','mon0','-wcoch.pcap'])
sleep(30)
p3.kill()
