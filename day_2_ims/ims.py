from collections import defaultdict
from itertools import groupby, combinations

from input import input_values as raw_input_values


# Part 1
input_values = (val for val in raw_input_values.split('\n') if val)

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



# Part 2
input_values = [val for val in raw_input_values.split('\n') if val]

curr_index = 0
word_len = len(input_values[0])

word_map = defaultdict(int)
while curr_index < word_len:
    chars = []
    for line in input_values:
        chars.append(line[curr_index])
    chars_indices = enumerate(chars)
    sorted_chars_indices = sorted(chars_indices, key=lambda x: x[1])
    groups = groupby(sorted_chars_indices, key=lambda x: x[1])
    for char, tuples in groups:
        indices = [t[0] for t in tuples]
        if len(indices) > 1:
            combies = list(combinations(indices, 2))
            for comb in combies:
                key = '{}-{}'.format(comb[0], comb[1])
                word_map[key] += 1
    curr_index += 1

final_indices = [k for k, v in word_map.items() if v == (word_len - 1)]
final_indices = final_indices[0].split('-')
word_1 = input_values[int(final_indices[0])]
word_2 = input_values[int(final_indices[1])]

final_word = ''
for i, j in zip(word_1, word_2):
    if i == j:
        final_word += i
print(final_word)
