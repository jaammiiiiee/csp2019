import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4
means_boys = (85, 87, 88.5, 93)
means_girls = (70, 78, 82, 90)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_boys, bar_width,
alpha=opacity,
color='skyblue',
label='Boys')

rects2 = plt.bar(index + bar_width, means_girls, bar_width,
alpha=opacity,
color='lightsalmon',
label='Girls')

plt.xlabel('Year')
plt.ylabel('Percent (%) of Primary School Age Children Enrolled')
plt.title('Students Enrolled in Primary School Over Time')
plt.xticks(index + bar_width, ('1980', '1990', '2000', '2010'))
plt.legend()

plt.tight_layout()
plt.show()