ip = "192.168.3.1"
ip1,ip2,ip3,ip4 = (ip.split("."))
print("%15s %15s %15s %15s" % (ip1 ,ip2 , ip3, ip4))

print("{:15}{:15}".format("{:08b}".format(int(ip1)) , "{:08}".format(int(ip2)) , "{:08b}".format(int(ip2)) , "{:08b}".format(int(ip3)) , "{:08b}".format(int(ip4))),
print("{:15}{:15}".format))