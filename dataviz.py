import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots()

#creat a pandas dataframe from a list
df = pd.DataFrame({'temp': [2015,2016,2017,2018,2019], 'year': [80,82,85,90,91]})

#plot the dataframe
ax.plot(df['temp'], df['year'], color='red',linestyle='--', marker='o')
#set the x and y labels
ax.set_xlabel('year')
ax.set_ylabel('temp')

#set the title
ax.set_title('December temps in FLL for various years')

plt.savefig('output.png')

#save the graph to a file
