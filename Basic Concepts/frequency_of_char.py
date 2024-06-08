def frequency_of_each_character(a):
    character_frequency_dict = {}
    for char in a:
        if char in character_frequency_dict:
            character_frequency_dict[char] += 1
        else:
            character_frequency_dict[char] = 1
    return character_frequency_dict

a = "Hyderabad"
output = frequency_of_each_character(a)
print(output) #output = {'H': 1, 'y': 1, 'd': 2, 'e': 1, 'r': 1, 'a': 2, 'b': 1}