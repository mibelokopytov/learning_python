with open('words.txt', 'r', encoding='utf-8') as file:
    l_words = [i for i in file.readline().split()]
    bigger = len(max(l_words, key=len))
    bigger_words = filter(lambda x: len(x) == bigger, l_words)
    for el in bigger_words:
        print(el)