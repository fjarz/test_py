import csv

import matplotlib.pyplot as plt

filename = 'storm_data_search_results.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    injuries = []
    for row in reader:
        INJURIES_INDIRECT = int(row[19])
        injuries.append(INJURIES_INDIRECT)
    
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(injuries, c='red')

plt.show()

