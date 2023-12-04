import pandas as pd
import numpy as np

df = pd.read_csv('Text Files/dec3.txt', header=None)
split_df = pd.DataFrame()

# Make a list to save indices of gears
gear_indices = []

# I want to make a grid representation of the engine schematic.
for i in range(df.shape[0]):
    row = df.iloc[i, :].values[0]
    split_row = []
    char_idx = 0
    for char in row:
        split_row.append(char)
        # If we come across a gear, save its location in the df
        if char == '*':
            gear_indices.append((i, char_idx))
        char_idx += 1
    df_row = pd.DataFrame(split_row).T
    split_df = pd.concat([split_df, df_row])

gear_ratio_sum = 0

# Now, I want to check for numbers around each gear index.
for idx in gear_indices:
    gear_number_list = []
    checked_idxs = []
    row, col = idx
    idx_check = [-1, 0, 1]
    for i in range(len(idx_check)):
        for j in range(len(idx_check)):
            check_row = row + idx_check[i]
            check_col = col + idx_check[j]
            current_check = split_df.iloc[check_row, check_col]
            # If we run into a number, we need to save the whole thing. Find where the number starts and ends.
            # But only do this if we haven't already seen this number.
            if current_check.isdigit() and (check_row, check_col) not in checked_idxs:
                found_ends = False
                found_end_right = False
                found_end_left = False
                end_right = check_col
                end_left = check_col
                r_idx = 0
                l_idx = 0
                while not found_ends:
                    end_right = end_right + 1
                    end_left = end_left - 1
                    try:
                        if not split_df.iloc[check_row, end_right].isdigit() and not found_end_right:
                            found_end_right = True
                            r_idx = end_right
                    except:
                        # We should hit this when we find a number that's at the edge of the df
                        found_end_right = True
                        r_idx = end_right
                    try:
                        if not split_df.iloc[check_row, end_left].isdigit() and not found_end_left:
                            found_end_left = True
                            l_idx = end_left + 1
                    except:
                        # We should hit this when we find a number that's at the edge of the df
                        found_end_left = True
                        l_idx = end_left + 1
                    if found_end_right and found_end_left:
                        found_ends = True
                part_digits = np.array(split_df.iloc[check_row, l_idx:r_idx])
                checked_idxs.append((check_row, l_idx))
                if len(part_digits) == 3:
                    part_number = int(part_digits[0]) * 100 + int(part_digits[1]) * 10 + int(part_digits[2])
                    checked_idxs.append((check_row, l_idx + 1))
                    checked_idxs.append((check_row, l_idx + 2))
                elif len(part_digits) == 2:
                    part_number = int(part_digits[0]) * 10 + int(part_digits[1])
                    checked_idxs.append((check_row, l_idx + 1))
                else:
                    part_number = int(part_digits[0])
                print(part_number)
                # Add the part number to our sum.
                gear_number_list.append(part_number)
    if len(gear_number_list) == 2:
        gear_ratio_sum += gear_number_list[0] * gear_number_list[1]

print(gear_ratio_sum)




