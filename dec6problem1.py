import numpy as np
import pandas as pd

df = pd.read_csv(r'Text Files\dec6.txt', header=None)

win_possibilities = []

# Iterate through each race
for i in range(df.shape[1]-1):
    race = i + 1
    record_time = df.iloc[0, race]
    record_dist = df.iloc[1, race]
    button_time = 0  # this will be your speed
    win_range = []
    win = False
    # Find minimum number of seconds you can hold button to win
    while not win:
        your_dist = button_time * (record_time - button_time)
        if your_dist > record_dist:
            win_range.append(button_time)
            win = True
        else:
            button_time += 1
    button_time = record_time
    win = False
    # Find maximum number of seconds you can hold button to win
    while not win:
        your_dist = button_time * (record_time - button_time)
        if your_dist > record_dist:
            win_range.append(button_time)
            win = True
        else:
            button_time -= 1
    # Every setting in between is also a possibility
    win_possibilities.append(win_range[1] - win_range[0] + 1)

print(win_possibilities)
print(np.prod(win_possibilities))