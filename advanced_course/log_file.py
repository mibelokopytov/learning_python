def time_check(a, b):
    a = a.strip().split(':')
    b = b.strip().split(':')

    if abs(int(a[0]) * 60 + int(a[1]) - (int(b[0]) * 60 + int(b[1]))) >= 60:
        return True
    else:
        return False


with open('logfile.txt', 'r', encoding='utf-8') as log_f, open('output.txt', 'w', encoding='utf-8') as out:
    content = [line.strip() for line in log_f.readlines()]
    for i in range(len(content)):
        content[i] = content[i].split(',')

    for el in content:
        if time_check(el[1], el[2]):
            print(el[0], file=out)