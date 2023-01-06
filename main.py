import numpy as np
import array
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from mpl_toolkits.mplot3d import Axes3D
import json

with open('ZWE_NGDPRPPPPC.json', 'r') as f:
    data = json.load(f)
dataset = data['dataset']
data_value = dataset['data']

print(f"there are {len(data_value)} data points") # get the  umber of records in the json file
print(f"the first element is {data_value[0]}")

# access all elements in the dataset
n = []
p = array.array('d', [])
for last_element in data_value[::1]:
    date = str(last_element[0])
    value = last_element[1]
    n.append(date)   # n.append(str(last_element[0])) could have worked also
    p.append(value)  # p.append(last_element[1]) could work as alternative

print(n)
print(p)
plt.bar(range(len(p)), p, color='blue')
plt.xticks(range(len(n)), n, rotation='vertical')
plt.grid()
plt.show()



