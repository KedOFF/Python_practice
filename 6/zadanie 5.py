command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
def lst(x):
    y=x.split(',')[-1]
    return  y.split(',')
print (set(lst(command1)+lst(command2)))