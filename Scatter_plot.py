import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('D:\AI&ML\mtcars.csv')

plt.scatter(df['wt'], df['mpg'])
plt.title('Scatter Plot of Weight vs MPG')
plt.xlabel('Weight (1000 lbs)')
plt.ylabel('MPG')
plt.grid(True)
plt.show()
