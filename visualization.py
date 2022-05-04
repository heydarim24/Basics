# data visualization ex
# matplotlib, pandas, seaborn

# import pandas as pd 
from matplotlib import pyplot as plt 

x = [1, 2, 3]
y = [1, 4, 9]
plt.plot(x, y) 
plt.show()


sample_data = pd.read_csv('Sample_Data.csv')
sample_data
type(sample_data)
#retrieve column 
sample_data.columnC.iloc[1] #get the second element 

plt.plot(sample_data.columnA, sample_data.columnB)
plt.show


