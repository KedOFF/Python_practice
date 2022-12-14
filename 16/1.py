import subprocess

def ping_ip_addresses(ip_list):
   
    alive_ip = []
    unreach_ip = []
    for ip in ip_list:
        command = subprocess.run(['ping', '{}'.format(ip), '-c', '3'], stdout=subprocess.DEVNULL)
        if command.returncode == 0:
            alive_ip.append(ip)
        else:
            unreach_ip.append(ip)
    ip_tuple = (alive_ip, unreach_ip)
    return ip_tuple

if __name__ == "__main__":
      ip_list = ["10.0.0.0", "255.255.0.1", "8.8.8.8"]
      ip_tuple = ping_ip_addresses(ip_list)
      print(ip_tuple)
