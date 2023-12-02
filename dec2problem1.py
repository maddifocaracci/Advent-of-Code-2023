import pandas as pd

df = pd.read_csv('dec2.csv', header=0)
game_list = df.iloc[:, 1:]

max_cubes = {'red': 12, 'green': 13, 'blue': 14}
possible_games = list(range(1, 101))

for game in game_list.iterrows():
    for round in game[1]:
        try:
            cube_list = round.split(',')
            for item in cube_list:
                x = item.split(' ')
                # Check if the number we see is over the max from our dict
                if int(x[1]) > max_cubes[x[2]]:
                    if game[0]+1 in possible_games:
                        possible_games.remove(game[0]+1)
        except:
            pass

print(sum(possible_games))
