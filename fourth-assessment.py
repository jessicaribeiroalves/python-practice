def get_n_longest_unique_words(words, n):
    longest_unique_words = []
    for item in words:
        if words.count(item) == 1:
            longest_unique_words.append(item)
    longest_unique_words.sort(key=len, reverse=True)
    return longest_unique_words[:n]


words = ['Whatever', 'Ball', 'Ball', 'Longest',
         'even longer', 'anyway', 'jess', 'anyway']
print(get_n_longest_unique_words(words, 3))
