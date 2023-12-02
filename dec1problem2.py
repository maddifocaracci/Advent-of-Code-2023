import pandas as pd

df = pd.read_csv('dec1problem1.csv', header=0)
value_list = df.iloc[:, 0]

total = 0
number_str = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for item in value_list:
    idx = 0
    numbers = []
    for i in item:
        if i.isdigit():
            # If the character is a digit, add to list
            numbers.append(int(i))
        else:
            # Check for three-letter numbers
            if item[idx:idx+3] in number_str:
                numbers.append(number_str[item[idx:idx+3]])
            # Check for four-letter numbers
            elif item[idx:idx+4] in number_str:
                numbers.append(number_str[item[idx:idx+4]])
            # Check for five-letter numbers
            elif item[idx:idx+5] in number_str:
                numbers.append(number_str[item[idx:idx + 5]])
        idx += 1
    calib_value = numbers[0] * 10 + numbers[-1]
    total += calib_value

print(total)