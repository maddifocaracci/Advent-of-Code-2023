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
    # card_values.sort(key=int)
    for j in range(len(card_values)):
        df.iloc[i, 3+j] = card_values[j]
    # TODO: Need a way to compare down to the last card
    # Now separate scores based on hand type
    if len(hand_dict.values()) == 1:
        score += 600
        print('5 of a kind')
    elif len(hand_dict.values()) == 2:
        if 4 in hand_dict.values():
            score += 500
            print('4 of a kind')
            # Find the card that's repeated 4 times
            # match = int(list(hand_dict.keys())[list(hand_dict.values()).index(4)])
            # nonmatch = int(list(hand_dict.keys())[list(hand_dict.values()).index(1)])
            # card_values = [nonmatch, match, match, match, match]
        if 3 in hand_dict.values():
            score += 400
            print('full house')
            # Find the card that's repeated 3 times
            # match = int(list(hand_dict.keys())[list(hand_dict.values()).index(3)])
            # nonmatch = int(list(hand_dict.keys())[list(hand_dict.values()).index(2)])
            # card_values = [nonmatch, nonmatch, match, match, match]
    elif len(hand_dict.values()) == 3:
        if 3 in hand_dict.values():
            score += 300
            print('3 of a kind')
            # Find the card that's repeated 3 times
            # match = int(list(hand_dict.keys())[list(hand_dict.values()).index(3)])
            # new_val_list = []
            # for card in card_values:
            #     if card != match:
            #         new_val_list.append(card)
            # card_values = new_val_list
            # card_values += [match, match, match]
        else:
            score += 200
            print('2 of a kind')
            # Find the two pairs
            # pairs = []
            # new_val_list = []
            # for card in card_values:
            #     if hand_dict[card] == 2:
            #         pairs.append(card)
            #     else:
            #         new_val_list.append(card)
            # card_values = new_val_list
            # pairs.sort(key=int)
            # card_values += pairs
    else:
        if 2 in hand_dict.values():
            score += 100
            print('one pair')
            # Find the card that's repeated
            # match = int(list(hand_dict.keys())[list(hand_dict.values()).index(2)])
            # new_val_list = []
            # for card in card_values:
            #     if card != match:
            #         new_val_list.append(card)
            # card_values = new_val_list
            # card_values += [match, match]
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

