import iperf3
clien = iperf3.Client()
clien.duration = 3
clien.server_hostname = '127.0.0.1'
clien.port = 5201
result = clien.run()
a = result.sent_Mbps
print(a)
