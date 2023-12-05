import pandas as pd
import math

df = pd.read_csv('dec5.csv', header=0)
print(df)

master_map = {}

# First set up a nested dictionary - each layer of the map has its own dictionary.
# For example, seed layer has a {seed value: soil value} mapping.
for col in range(df.shape[1]):
    master_map[col] = {}
    for i in range(df.shape[0]):
        key = df.iloc[i, col]
        if type(key) == str:
            # This is how we now we're not in the first (seed) layer
            key = key.split()
            dest_start = int(key[0])
            source_start = int(key[1])
            range_len = int(key[2])
            # Go through each object in the previous layer of the map
            for item in master_map[col-1]:
                if source_start < item < source_start + range_len:
                    # If the object is in range, connect it to the previous map layer's dictionary
                    dest_num = dest_start + item - source_start
                    master_map[col-1][item] = dest_num
                    # Add the object's value to our current map layer
                    master_map[col][dest_num] = 'placeholder'
                    break
                    # Need not just the first mapping we find but ALL possible mappings
                    # Need to use lists instead of placeholders
        elif not math.isnan(key):
            master_map[col][int(key)] = 'placeholder'
    # If one of the items in our previous layer has no mapping, drop it from the dict
    if col > 0:
        del_keys = []
        for item in master_map[col-1]:
            if master_map[col-1][item] == 'placeholder':
                del_keys.append(item)
        for item in del_keys:
            del master_map[col-1][item]

# Grab the minimum value from the last layer.
print(min(master_map[df.shape[1]-1]))

min_location = 1e30


