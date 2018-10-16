#install killall using apt-get install psmisc
import SerialComm
from time import sleep
ser = SerialComm.SerialComm(port='/dev/ttyUSB0', baudrate=115200, timeout=1)
print ser.login_status()
ser.login('root', 'zilogic')
print ser.login_status()
ser.sendline("iw phy phy0 interface add mon0 type monitor")
ser.sendline("ifconfig mon0 up")
ser.sendline("tshark -i mon0 -w wire1.pcap &")
sleep(300)
ser.sendline("killall -9 tshark")
ser.sendline("tshark -i mon0 -w wire1.pcap &")
sleep(300)
ser.sendline("killall -9 tshark")
ser.sendline("tshark -i mon0 -w wire1.pcap &")
sleep(300)
ser.sendline("killall -9 tshark")
ser.logout()

