from collections import namedtuple
from itertools import*

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

value = int(input())

if min(items, key= lambda x: x.mass).mass > value:
    print('Рюкзак собрать не удастся')
else:
    data = chain.from_iterable(combinations(items, r=i) for i in range(11))
    data_filtered = filter(lambda x: value >= sum(i.mass for i in x), data)
    result = max(data_filtered, key=lambda x: sum(i.price for i in x))
    print(*sorted(i.name for i in result), sep='\n')