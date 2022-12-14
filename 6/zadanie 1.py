i=0
nat = ["ip", "nat", "inside source list ACL interface", "FastEthernet0/1", "overload"]
if "FastEthernet0/1" in nat:
    i=nat.index("FastEthernet0/1")
    nat[1] = "GigabitEthernet"
elif "GigabitEthernet" in nat:
    print("nat")
print(nat)
