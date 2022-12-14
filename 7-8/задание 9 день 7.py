access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

template = {'access': access_template, 'trunk': trunk_template}
question = {'access': 'VLAN: ', 'trunk': ' VLANС‹:'}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlan = input(f"{question[mode]}")

print(f"interface {interface}")
print('\n'.join(template[mode]).format(vlan))