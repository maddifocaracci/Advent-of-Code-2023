import pandas as pd
import math

df = pd.read_csv('dec5.csv', header=0)
num_cols = df.shape[1]

master_map = {}

# I literally cannot consider every seed. What I NEED to do is find possible ranges of seeds.

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
            source_end = source_start + range_len - 1
            # Go through each item in the previous layer of the map
            for item in master_map[col-1]:
                # Now, item will have a range instead of just one value.
                # We need to find the LIMITS that will work.
                item_start = item[0]
                item_end = item[1]
                if source_start <= item_start <= source_end and source_start <= item_end <= source_end:
                    # The entire item is in range
                    next_start = dest_start + item_start - source_start
                    next_end = dest_start + item_end - source_start
                    master_map[col-1][item] += [next_start, next_end]
                    master_map[col][next_start, next_end] = []
                elif source_start <= item_start <= source_end:
                    # Only the start of the item is in range
                    next_start = dest_start + item_start - source_start
                    next_end = dest_start + range_len - 1
                    master_map[col-1][item] += [next_start, next_end]
                    # Add the whole item range to our current map layer
                    master_map[col][next_start, next_end] = []
                    # We ALSO need an entry for the part of the item that gets cut off
                    # cutoff_start = source_end - item_start
                    master_map[col][source_end+1, item_end] = []
                elif source_start <= item_end <= source_end:
                    # Only the end of the item is in range
                    next_start = dest_start
                    next_end = dest_start + item_end - source_start
                    master_map[col-1][item] += [next_start, next_end]
                    # Add the whole item range to our current map layer
                    master_map[col][next_start, next_end] = []
                    # We ALSO need an entry for the part of the item that gets cut off
                    # cutoff_end = item_end - source_start
                    master_map[col][item_start, source_start-1] = []
        elif not math.isnan(key):
            if i % 2 == 0:
                # If we're on a seed number rather than a range
                start_seed = int(key)
                end_seed = int(key) + int(df.iloc[i+1, col]) - 1
                # Put the range of seed numbers into the dict
                master_map[col][start_seed, end_seed] = []
    if col > 0:
        # If one of the items in our previous layer has no mapping, give it same number in current layer
        for item in master_map[col-1]:
            if len(master_map[col-1][item]) < 1:
                master_map[col-1][item] = [item]
                master_map[col][item] = []

# Grab the minimum value from the last layer.
print(min(master_map[df.shape[1]-1]))

print('hello')


