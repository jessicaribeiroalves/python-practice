def positive_even_squares(*args):
    result = []
    for lst in args:
        filtered = filter(lambda x: (x > 0 and x % 2 == 0), lst)
        squares = map(lambda x: (x ** 2), filtered)
        for square in squares:
            result.append(square)

    return result
