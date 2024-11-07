from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)

    def add(self, num):
        self.iterable.append(num)

    def clear(self):
        self.iterable.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        if len(self.iterable) > 0:
            return min(self.iterable)


class MaxStat(Stat):
    def result(self):
        if len(self.iterable) > 0:
            return max(self.iterable)


class AverageStat(Stat):
    def result(self):
        if len(self.iterable) > 0:
            return sum(self.iterable) / len(self.iterable)