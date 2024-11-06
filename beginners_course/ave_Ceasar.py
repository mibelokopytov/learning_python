rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lower_alphabet = eng_lower_alphabet
upper_alphabet = eng_upper_alphabet

def cesar_code(text, rot_na_oborot, total):


        for i in range(len(text)):
            if text[i].isalpha():

                if text[i] == text[i].lower():
                    place = lower_alphabet.index(text[i])
                if text[i] == text[i].upper():
                    place = upper_alphabet.index(text[i])

                ind = (place + rot_na_oborot) % total

                if text[i] == text[i].lower():
                    print(lower_alphabet[ind], end='')
                if text[i] == text[i].upper():
                    print(upper_alphabet[ind], end='')
            else:
                 print(text[i], end='')


def text_el_rot(text):
    text_rot = []
    counter = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                counter += 1
        text_rot.append(counter)
        counter = 0
    return text_rot


text = input().split()
text_el_rot(text)
total = 26
for i in range(len(text)):
    rot_na_oborot = text_el_rot(text)[i]
    cesar_code(text[i], rot_na_oborot, total)
    print(end=" ")