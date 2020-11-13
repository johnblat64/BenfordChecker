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
        histogram[str(digit)] = data[digit - 1] / total_count
    
    return histogram

if len(sys.argv) < 3:
    print('Usage: benford.py <filename> <column-to-create-benford-graph-on>')

filename = sys.argv[1]
column_name = sys.argv[2]
encoding = sys.argv[3] if len(sys.argv) > 3 else 'iso-8859-1'

fields = [column_name]
data = pd.read_csv(filename, sep=',', usecols=fields, encoding=encoding)

total_count, data_count  = count_first_digit(column_name, data)
# data_count_df = DataFrame(data_count, columns=[''])
# print("\nobserved counts = {}".format(data_count))
histogram = create_histogram(data_count, total_count)
plt.bar(range(len(histogram)), list(histogram.values()), align='center')
plt.xticks(range(len(histogram)), list(histogram.keys()))

for digit in range(1,10):
    print("digit: "+ str(digit) + ", percentage: "+ str(histogram[str(digit)] * 100) + "%")
    
plt.show()

