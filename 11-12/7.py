#задание 7
vlan = input('Enter VLAN ID: ')

with open('CAM_table.txt') as cam:
    file = cam.readlines()
    for line in file:
        if '.' in line:
            line_list = line.split()
            line_list.remove('DYNAMIC')
            if line_list[0] == vlan:
                print("   ".join(line_list))