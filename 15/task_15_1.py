


def parse_cdp_neighbors(command_output):

    lines = command_output.strip().split('\n')
    interest = False
    result = {}
    for line in lines:
        if interest:
            neigh,lint,linum,to,*cap,plat,nint,ninum = line.split()
            result[(dev, lint+linum)] = (neigh, nint+ninum)
        else:
            if line.startswith('Device ID'):
                interest = True
            elif ' cdp nei' in line:
                dev = line.replace('#', '>').split('>')[0]
    return(result)


if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))
