class Fibonacci:
    def __init__(self):
        self.current_index = 0
        self.cache = {1: 1, 2: 1}

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        result = self.cache.get(self.current_index)
        if result is None:
            first = self.cache[self.current_index - 2]
            second = self.cache[self.current_index - 1]
            first, second = second, second + first
            result = second
            self.cache[self.current_index] = result
        return result