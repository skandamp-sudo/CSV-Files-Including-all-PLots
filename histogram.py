import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('D:\AI&ML\mtcars.csv')

plt.hist(df['mpg'], bins=10, edgecolor='black')
plt.title('Histogram of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

hist, bin_edges = np.histogram(df['mpg'], bins=10)
max_freq_bin = bin_edges[np.argmax(hist)]
max_freq_bin
