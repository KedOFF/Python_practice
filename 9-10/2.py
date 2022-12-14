ip = input("Input IP: ")
ip_list = ip.split(".")
oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]
if oct1 >= 1 and oct1 <= 223:
    print ("unicast")
elif oct1 >= 224 and oct1 <= 239:
    print ("multicast")
elif ip == '255.255.255.255':
    print ("local broadcast")
elif ip == '0.0.0.0':
    print ("unassigned")
else:
    print ("unused")