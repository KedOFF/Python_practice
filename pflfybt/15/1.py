def parse_cdp_neighbors(command_output):

    result = {}

    command = command_output.strip()

    local_host = command[0:command.find('>')]

    neighbors = command[command.find('ID\n') + 3 ::]
    neighbors = neighbors.split('\n')

    for line in neighbors:
        line = line.split()
        r_host, l_intf, l_intf_num, *other, r_intf, r_intf_num = line
        r_intf = r_intf + r_intf_num
        l_intf = l_intf + l_intf_num
        result[local_host, l_intf] = r_host, r_intf

    return(result)


if __name__ == '__main__':
    file = open('sh_cdp_n_sw1.txt', 'r')
    result =  parse_cdp_neighbors(file.read())

    file.close()

    print(result)
