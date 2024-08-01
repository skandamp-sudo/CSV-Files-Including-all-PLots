import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('D:\AI&ML\mtcars.csv')

plt.boxplot(df['mpg'])
plt.title('Box Plot of MPG')
plt.ylabel('MPG')
plt.grid(True)
plt.show()

five_number_summary = df['mpg'].describe()[['min', '25%', '50%', '75%', 'max']]
five_number_summary
