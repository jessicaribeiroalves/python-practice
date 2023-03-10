def generate_string(string, frequency):
    i = 0
    while i < len(string):
        x = string[i] * frequency
        yield x
        i += 1


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.string):
            x = self.string[self.i] * self.frequency
            self.i += 1
            return x
        raise StopIteration
