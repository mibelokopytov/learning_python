def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        file_lines = (line.rstrip('\n') for line in file)
        temp_dict = dict()
        dict_list = []
        for line in file_lines:
            if line != '':
                key, value = [x.strip() for x in line.split('=')]
                temp_dict.setdefault(key, value)

            else:
                dict_list.append({key: value for key, value in temp_dict.items()})
                temp_dict.clear()
                continue
        dict_list.append({key: value for key, value in temp_dict.items()})

        for planet in dict_list:
            yield planet