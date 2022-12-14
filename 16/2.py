from ipaddress import ip_address

def convert_ranges_to_ip_list(ip_list):
  
    full_list = []
    for ip in ip_list:
        if "-" in ip:
            divide_ip = ip.split("-")
            first_ip = ip_address(divide_ip[0])
            last_ip = divide_ip[1]
            if len(last_ip.split(".")) != 1:
                last_ip = ip_address(last_ip)
                range_ip = list(range(int(first_ip), (int(last_ip) + 1)))
            else:
                replace_ip = divide_ip[0].split(".")
                replace_ip[3] = divide_ip[1]
                last_ip = ip_address(".".join(replace_ip))
                range_ip = list(range(int(first_ip), (int(last_ip)+1)))
            for item in range_ip:
                new_ip = str(ip_address(item))
                full_list.append(new_ip)
        else:
            full_list.append(ip)
    return full_list

if __name__ == "__main__":
    print(convert_ranges_to_ip_list(["8.8.8.8", "192.168.0.1-10", "172.10.0.1-172.10.0.15"]))
