from sys import argv

file_in = argv[0]
with open(file_in) as src:
    for line in src:
        if not line.startswith('!'):
            print(line.rstrip())