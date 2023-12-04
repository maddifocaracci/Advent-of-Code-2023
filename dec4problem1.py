import pandas as pd

df = pd.read_csv('dec4.csv', header=None)

winnings = 0

for i in range(df.shape[0]):
    card_power = 0
    your_numbers = df.iloc[i, 2].split()
    winning_numbers = df.iloc[i, 1].split()
    for num in your_numbers:
        if num in winning_numbers:
            card_power += 1
    if not card_power:
        pass
    else:
        winnings += 1 * 2 ** (card_power - 1)

print(winnings)
