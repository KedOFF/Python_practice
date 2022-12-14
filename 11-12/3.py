from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
file_in = argv[0]
with open(file_in) as src:
    for line in src:
        if not line.startswith('!'):
            for ig in ignore:
                if ig in line:
                    break
            else:
                print(line.rstrip())