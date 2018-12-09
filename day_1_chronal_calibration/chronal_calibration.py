from input import raw_values


raw_values = [val for val in raw_values.split('\n') if val]
final_frequency = 0
frequencies = set()
done = False

while not done:
    for input_value in raw_values:
        value = int(input_value[1:])
        if '+' in input_value:
            final_frequency += value
        if '-' in input_value:
            final_frequency -= value
        if final_frequency in frequencies:
            done = True
            break
        else:
            frequencies.add(final_frequency)

print(len(frequencies))
print(final_frequency)
