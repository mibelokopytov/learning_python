from collections.abc import Sequence
from copy import deepcopy


class BitArray(Sequence):
    def __init__(self, iterable=[]):
        if len(iterable) > 0:
            self.iterable = deepcopy(iterable)
        else:
            self.iterable = iterable

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.iterable[item]

    def __len__(self):
        return len(self.iterable)

    def __invert__(self):
        return BitArray([1 if i == 0 else 0 for i in self.iterable])

    def __str__(self):
        return f'{self.iterable}'

    def __and__(self, other):
        if isinstance(other, BitArray):
            if len(self) == len(other):
                return BitArray([a & b for a, b in zip(self, other)])
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, BitArray):
            if len(self) == len(other):
                return BitArray([a | b for a, b in zip(self, other)])
        return NotImplemented