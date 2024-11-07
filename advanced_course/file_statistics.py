with open('file.txt', encoding='utf-8') as file:
    line = file.readline()
    counter_st = 0
    while line != '':
        counter_st += 1
        line = file.readline()
    file.seek(0)
    content = file.read().split()
    file.seek(0)
    letters = [i for i in file.read() if i.isalpha()]
    print('Input file contains:')
    print(len(letters), 'letters')
    print(len(content), 'words')
    print(counter_st, 'lines')