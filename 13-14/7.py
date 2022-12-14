
ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):

    return any(word in command for word in ignore)

def cfg_to_dict(config):
    result = {}
    with open(config) as file:
        for line in file:
            if ignore_command(line, ignore) or line.startswith('!'):
                pass
            else:
                if not line.startswith(' '):
                    key = line.strip()
                    result[key] = []
                else:
                    result[key].append(line.strip())

    return result

result = cfg_to_dict('config_sw1.txt')

for key, values in result.items():
    print('{} : {}'.format(key, values))