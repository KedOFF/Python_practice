network = input("Введите ip-сеть в формате a.a.a.a/b""\n")

ip, mask = network.split("/")
ip_list = ip.split(".")
mask = int(mask)

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

bin_ip= '{:08b}{:08b}{:08b}{:08b}'.format(oct1, oct2, oct3, oct4)
bin_network = bin_ip[0:mask] + "0" * (32 - mask)

network_oct1, network_oct2, network_oct3, network_oct4 = [
    int(bin_network[0:8], 2),
    int(bin_network[8:16], 2),
    int(bin_network[16:24], 2),
    int(bin_network[24:32], 2),
]

print(oct1, oct2, oct3, oct4)
print(bin_ip)
print(bin_network)

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]
print (bin_mask)
print(m1, m2, m3, m4)




ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(network_oct1, network_oct2, network_oct3, network_oct4))
print(mask_output.format(mask, m1, m2, m3, m4))