from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
file_out = 'config_sw1_cleared.txt'
file_in = argv[0]
with open(file_in) as src, open(file_out, 'a') as dst:
    for line in src:
        for ig in ignore:
            if ig in line:
                break
        else:
            dst.write(line)

