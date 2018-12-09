from collections import defaultdict

from input import input_values

# input_values = '''
# abcdef
# bababc
# abbcde
# abcccd
# aabcdd
# abcdee
# ababab
# '''

input_values = (val for val in input_values.split('\n') if val)

num_double_words = 0
num_triple_words = 0
for input_value in input_values:
    letter_frequencies = defaultdict(int)
    for letter in input_value:
        letter_frequencies[letter] += 1

    has_double_word = False
    has_triple_word = False
    for letter, frequency in letter_frequencies.items():
        if frequency == 2:
            has_double_word = True
        elif frequency == 3:
            has_triple_word = True
    if has_double_word:
        num_double_words += 1
    if has_triple_word:
        num_triple_words += 1

print(num_double_words * num_triple_words)
