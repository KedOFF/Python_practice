from sys import argv
#file_read = str(argv)
file_read = 'CAM_table.txt'
with open(file_read) as file:
    for line in file:
        list = line.split()
        for item in list:
           if len(item.split('.')) == 3:
               print('{} {:>17} {:>9}'.format(list[0], list[1], list[3]))
