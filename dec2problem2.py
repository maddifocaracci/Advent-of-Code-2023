import pandas as pd

df = pd.read_csv('dec2.csv', header=0)
game_list = df.iloc[:, 1:]

total_power = 0

for game in game_list.iterrows():
    game_min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for round in game[1]:
        try:
            cube_list = round.split(',')
            for item in cube_list:
                x = item.split(' ')
                # In each round, if we see more cubes than have come up before,
                # That's the new minimum number we need for that game.
                if int(x[1]) > game_min_cubes[x[2]]:
                    game_min_cubes[x[2]] = int(x[1])
        except:
            pass
    # After all the rounds, we find the power of that game and add to our sum
    game_power = 1
    for cube_color in game_min_cubes:
        game_power *= game_min_cubes[cube_color]
    total_power += game_power

print(total_power)


