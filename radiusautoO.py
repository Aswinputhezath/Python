from time import sleep
import Hostapd
AP2 = Hostapd.Hostapd("AP.conf","172.16.2.150")
AP2.channel('1')
AP2.driver("nl80211")
AP2.interface("wlan3")
AP2.ap_ssid("CCI")
AP2.mode("b")
AP2.auth_algs("3")
AP2.wpa_key_mgmt("WPA2-PSK")
AP2.wpa_pairwise("CCMP")
AP2.wpa_passphrase("123456789")
AP2.serve_ap("start")
AP2.auth_server("198.168.1.1","1812")


#sleep(10000)
#AP2.serve_ap("stop")
AP1 = Hostapd.Hostapd("AP.conf","172.16.2.180")
chnl = 1
for i in range(2):
        AP1.channel(chnl)
        AP1.driver("nl80211")
        AP1.interface("wlan3")
        AP1.ap_ssid("ASI")
        AP1.mode("b")
        AP1.auth_algs("3")
        AP1.wpa_key_mgmt("WPA2-PSK")
        AP1.wpa_pairwise("CCMP")
        AP1.wpa_passphrase("123456789")
        AP1.serve_ap("start")
        sleep(50)
        AP1.serve_ap("stop")
        chnl+=2

