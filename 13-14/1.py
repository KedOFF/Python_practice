def generate_access_config(access):
 
    result = []
    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    for intf, vlan in access.items():
        result.append('interface ' + intf)
        for line in access_template:
            if line.endswith('vlan'):
                result.append(line + " " + str(vlan))
            else:
                result.append(line)
    return result


access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

result = generate_access_config(access_dict)
print(result)

print('=' * 30)

for line in result:
    print(line)