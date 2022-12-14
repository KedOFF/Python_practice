with open('CAM_table.txt') as cam:
    result_lol = []
    for line in cam:
        if '.' in line:
            line_list = line.strip().split()
            line_list.remove('DYNAMIC')
            result_lol.append(line_list)

            # Сортировка списка result_lol по числу в начале строки
    result_lol.sort(key=lambda x: int(x[0]))

    for list in result_lol:
        print('   '.join(list))