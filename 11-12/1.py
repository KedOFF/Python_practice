
ospf_route = "0 10.0.24.0/24 [110/41] 10.0.13.3, 3d18h, FastEthernet0/0"

s = ospf_route.split()
# печать
s_protocol = s[0].replace("0", "OSPF")
s_prefix = s[1]
s_metric = s[2]
s_metric = s_metric[1:-1]
s_next_hop = s[3]
s_next_hop = s_next_hop[:-1]
s_last_upd = s[4]
s_last_upd = s_last_upd[:-1]
s_interface = s[5]


print('Prefix:', '{:>35}'.format(s_prefix))
print('AD/Metric:', '{:>26}'.format(s_metric))
print('Next-Hop:', '{:>30}'.format(s_next_hop))
print('Last Update:', '{:>23}'.format(s_last_upd))
print('Outbound:', '{:>26}'.format(s_interface))

ospf_route = "0 10.0.24.0/24 [110/41] 10.0.13.3, 3d18h, FastEthernet0/0"
info = ['Protocol:' 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'OurBound Interface:']
s = ospf_route.split()
print("interface")


