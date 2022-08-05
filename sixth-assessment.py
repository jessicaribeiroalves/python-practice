# if frequency is enough to create both strings without reusing any chars -> return 2
# if frequency is enough to create string1 or string2 without reusing any chars -> return 1
# if frequency is not enough to create string1 or string2 without reusing any chars -> return 0

def check_if_string_can_be_written(frequencies, string):
    string_frequencies = {}
    for char in string:
        string_frequencies[char] = string_frequencies.get(char, 0) + 1
    for char, frequency in string_frequencies.items():
        if frequency > frequencies.get(char, 0):
            return False
    return True


def create_strings_from_characters(frequencies, string1, string2):

    if check_if_string_can_be_written(frequencies, string1 + string2):
        return 2
    elif check_if_string_can_be_written(frequencies, string1) or check_if_string_can_be_written(frequencies, string2):
        return 1
    else:
        return 0


frequencies = {
    'h': 2,
    'e': 1,
    'l': 1,
    'r': 4,
    'a': 3,
    'o': 2,
    'd': 1,
    'w': 1
}

string1 = 'hello'
string2 = 'world'

print(create_strings_from_characters(frequencies, string1, string2))
# it should return 1
