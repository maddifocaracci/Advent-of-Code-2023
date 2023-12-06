import numpy as np
import pandas as pd

# This time, there's only one race

record_time = 41968894
record_dist = 214178911271055
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
win_possibilities = win_range[1] - win_range[0] + 1

print(win_possibilities)