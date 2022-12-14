# задание 6
with open('CAM_table.txt') as cam:
    result_lol = []
    for line in cam:
        if '.' in line:
            line_list = line.strip().split()

            line_list.remove('DYNAMIC')
            line_list.sort()
            print('   '.join(line_list))

#for list in line_list:
 #   print('   '.join(list))
