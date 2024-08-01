import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('D:\AI&ML\mtcars.csv')

transmission_counts = df['am'].value_counts()
transmission_labels = ['Automatic', 'Manual']

plt.bar(transmission_labels, transmission_counts, color=['blue', 'orange'])
plt.title('Frequency Distribution of Transmission Types')
plt.xlabel('Transmission Type')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
