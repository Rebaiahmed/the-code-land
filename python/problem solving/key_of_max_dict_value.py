# Below are two implementations for getting the key of the max value in a dictionary.

sample_dict = {'Turtles':5, 'Dogs':3, 'Cats':3, 'Snakes':2}
max_key = max(sample_dict, key=sample_dict.get)
print(f"In the dictionary, there are the most {max_key} ({sample_dict[max_key]}).")

# Result
# In the dictionary, there are the most Turtles (5).


sample_dict = {'Turtles':5, 'Dogs':3, 'Cats':3, 'Snakes':2}
max_value = 0

for key in sample_dict:
    if sample_dict[key] > max_value:
        max_value = sample_dict[key]
        max_key = key

print('In the dictionary, there are the most ' + str(max_key) + ' (' + str(max_value) + ').')

# Result
# In the dictionary, there are the most Turtles (5).
