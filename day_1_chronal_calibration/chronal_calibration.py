from input import raw_values

# raw_values = '''
# +1
# -50
# +1
# '''

raw_values = [val for val in raw_values.split('\n') if val]

final_frequency = 0
for input_value in raw_values:
    value = int(input_value[1:])
    if '+' in input_value:
        final_frequency += value
    if '-' in input_value:
        final_frequency -= value
print(final_frequency)
