ip_good = False
while not ip_good:
    ip_good = True
    ip = input("Input IP: ")
    ip_list = ip.split(".")
    if len(ip_list) != 4:
        ip_good = False

    for oct in ip_list:
        if not (oct.isdigit() and int(oct) in range(255)):
            ip_good = False

    if not ip_good:
        print
        "Bad IP"
    else:
        oct1, oct2, oct3, oct4 = [
            int(ip_list[0]),
            int(ip_list[1]),
            int(ip_list[2]),
            int(ip_list[3]),
        ]
        if oct1 >= 1 and oct1 <= 223:
            print("unicast")
        elif oct1 >= 224 and oct1 <= 239:
            print("multicast")
        elif ip == '255.255.255.255':
            print("local broadcast")
        elif ip == '0.0.0.0':
            print("unassigned")
        else:
            print("unused")