import pandas as pd

df = pd.read_csv('dec1problem1.csv', header=0)
value_list = df.iloc[:, 0]

total = 0

for item in value_list:
    numbers = [int(i) for i in item if i.isdigit()]
    calib_value = numbers[0] * 10 + numbers[-1]
    total += calib_value

print(total)