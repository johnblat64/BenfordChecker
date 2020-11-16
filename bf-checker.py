import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import sys

def count_first_digit(column_name, data):
    mask = data[column_name] > 1
    new_data = list(data[mask][column_name])

    for i in range(len(new_data)):
        while new_data[i]>10:
            new_data[i] = new_data[i]/10
    first_digits = [int(x) for x in sorted(new_data)]
    unique=(set(first_digits))
    data_count=[]
    for i in unique:
        count=first_digits.count(i)
        data_count.append(count)
    total_count=sum(data_count)
    #data_percentage=[(i/total_count) * 100 for i in data_count]
    return total_count, data_count

def create_histogram(data, total_count):
    histogram = {}
    for digit in range(1,10):
        histogram[str(digit)] = (data[digit - 1] / total_count) * 100
    
    return histogram

benfords_law = {
    "1": 30.1,
    "2": 17.6,
    "3": 12.5,
    "4": 9.7,
    "5": 7.9,
    "6": 6.7,
    "7": 5.8,
    "8": 5.1,
    "9": 4.6
}


if len(sys.argv) < 3:
    print('Usage: benford.py <filename> <column-to-create-benford-graph-on>')

filename = sys.argv[1]
column_name = sys.argv[2]
encoding = sys.argv[3] if len(sys.argv) > 3 else 'iso-8859-1'

fields = [column_name]

data = pd.read_csv(filename, sep=',', usecols=fields, encoding=encoding)
total_count, data_count  = count_first_digit(column_name, data)
histogram = create_histogram(data_count, total_count)

width = 0.3

plt.title('Check against Benford\'s law')
plt.xlabel('Leading Digit')
plt.ylabel('Percentage in data set')
plt.xticks(range(len(histogram)), list(histogram.keys()))
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.3)
plt.bar(range(len(benfords_law)), list(benfords_law.values()), width=width, label='Benford\'s Law Value')
plt.bar(np.arange(len(histogram)) + width, list(histogram.values()), width=width, label='Input Dataset Value')
plt.legend()


for digit in range(1,10):
    print("digit: "+ str(digit) + ", percentage: "+ str(histogram[str(digit)] ) + "%")
    
plt.show()

