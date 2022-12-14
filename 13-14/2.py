def generate_access_config(access, psecurity=False):

    result = []
    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    for intf, vlan in access.items():
        result.append('interface ' + intf)
        for line in access_template:
            if line.endswith('vlan'):
                result.append(line + ' ' + str(vlan))
            else:
                result.append(line)
        if psecurity:
            for line in port_security:
                result.append(line)
    return result


access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

result = generate_access_config(access_dict, psecurity=True)
print(result)

print('=' * 30)

for line in result:
    print(line)