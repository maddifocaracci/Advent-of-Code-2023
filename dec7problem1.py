import numpy as np
import pandas as pd

df = pd.read_csv(r'Text Files\dec7.txt', header=None)

# Add column to keep track of card scores
df['Score'] = ''
df['Fifth'] = ''
df['Fourth'] = ''
df['Third'] = ''
df['Second'] = ''
df['First'] = ''
print(df.dtypes)
score_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

for i in range(df.shape[0]):
    hand = df.iloc[i, 0]
    hand_dict = {}
    score = 0
    card_values = []
    # Add to the hand score based on card values
    for card in hand:
        if card.isdigit():
            card = int(card)
            card_values.append(card)
        else:
            card = score_dict[card]
            card_values.append(card)
        if card not in hand_dict:
            hand_dict[card] = 1
        else:
            hand_dict[card] += 1
    for j in range(len(card_values)):
        df.iloc[i, 3+j] = card_values[j]
    # Now separate scores based on hand type
    if len(hand_dict.values()) == 1:
        score += 600
        print('5 of a kind')
    elif len(hand_dict.values()) == 2:
        if 4 in hand_dict.values():
            score += 500
            print('4 of a kind')
        if 3 in hand_dict.values():
            score += 400
            print('full house')
    elif len(hand_dict.values()) == 3:
        if 3 in hand_dict.values():
            score += 300
            print('3 of a kind')
        else:
            score += 200
            print('2 of a kind')
    else:
        if 2 in hand_dict.values():
            score += 100
            print('one pair')
        else:
            print('high card')
    for j in range(len(card_values)):
        df.iloc[i, 3+j] = card_values[4-j]
    df.iloc[i, 2] = score

# Sort hands according to rank
ranked_df = df.sort_values(['Score', 'First', 'Second', 'Third', 'Fourth', 'Fifth'])

total_winnings = 0

# Now, find total winnings by multiplying bid and rank
for i in range(ranked_df.shape[0]):
    rank = i + 1
    bid = ranked_df.iloc[i, 1]
    total_winnings += rank * bid

print(total_winnings)

