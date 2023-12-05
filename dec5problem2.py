import pandas as pd
import math

df = pd.read_csv('dec5.csv', header=0)
num_cols = df.shape[1]

master_map = {}

# Starting with the last layer, we want to build up possible ranges of values in the next layer
for i in range(num_cols):
    current_col = num_cols - i - 1
    master_map[current_col] = {}
    current_layer = df.iloc[:, current_col][0].split()
    current_start = int(current_layer[0])
    prev_start = int(current_layer[1])
    prev_range = int(current_layer[2])
    prev_max = prev_start + prev_range
    master_map[current_col][current_start] = [prev_start, prev_max]



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
                    master_map[col-1][item].append(dest_num)
                    # Add the object's value to our current map layer
                    master_map[col][dest_num] = []
        elif not math.isnan(key):
            if i % 2 == 0:
                # If we're on a seed number rather than a range
                start_seed = int(key)
                seed_range = int(df.iloc[i+1, col])
                # Add a seed to the initial dict for every num in this range
                for k in range(seed_range):
                    seed_num = start_seed + k
                    master_map[col][seed_num] = []
    if col > 0:
        # If one of the items in our previous layer has no mapping, give it same number in current layer
        for item in master_map[col-1]:
            if len(master_map[col-1][item]) < 1:
                master_map[col-1][item] = [item]
                master_map[col][item] = []

# Grab the minimum value from the last layer.
print(min(master_map[df.shape[1]-1]))

# I literally cannot consider every seed. What I NEED to do is find possible ranges of seeds. I should do this by
# working backwards. I find all the possible ranges of values in the previous layer. Work back until you get
# to the seed layer.


