
def generate_trunk_config(trunk):

    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]

    result = {}

    for intf, vlans in trunk.items():
        result[intf] = []
        for line in trunk_template:
            if line.endswith('vlan'):
                result[intf].append(line + ' ' + ','.join([str(vlan) for vlan in vlans]))
            else:
                result[intf].append(line)

    return result


trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

result = generate_trunk_config(trunk_dict)
print(result)