import string


def caesar_cipher(my_string, offset):
    alphabet = list(string.ascii_lowercase)
    new_string = ''
    for char in my_string:
        new_char_index = alphabet.index(char) - offset
        new_char = alphabet[new_char_index]
        new_string += new_char
    return new_string


print(caesar_cipher('jessica', 2))
# should return 'hcqqgay'
print(caesar_cipher('amazonia', 3))
# should return 'xjxwlkfx'
