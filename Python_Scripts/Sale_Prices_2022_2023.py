import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
x = pd.read_csv("2023_Final.csv")
y = pd.read_csv("2022_Final.csv")


x = x.drop(columns=['lat','lon','Municipality'])
y = y.drop(columns=['lat','lon','Municipality'])
mean_x = x.mean()
print("Mean of dataset x:", mean_x)
#find the mean of 2023 data set
mean_y = y.mean()
print("Mean of dataset y:", mean_y)
#fine the mean of 2022 data set 
y = y[y['Sale price'] != 0] 
x = x[x['Sale price'] != 1] 
#drop all the 0 and 1's 

fig, ax = plt.subplots(dpi=300)
data = [y['Sale price'], x['Sale price']]
labels = ['2022', '2023']
ax.boxplot(data, labels=labels, showfliers=False)
ax.axhline(mean_x, color='red', linestyle='--', label='Mean 2022')
ax.axhline(mean_y, color='blue', linestyle='--', label='Mean 2023')
ax.set_title('Average Sale Prices for 2022 vs. 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Sale Price ($)')
ax.legend()
plt.show()
fig.savefig('prices.png')
#produce a boxplot