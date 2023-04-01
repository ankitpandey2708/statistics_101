import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = []

# Calculate statistical values
mean = np.mean(data)
median = np.median(data)
minimum = np.min(data)
maximum = np.max(data)
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
upper_bound = q3 + (1.5 * iqr)
lower_bound = q1 - (1.5 * iqr)
outliers = [x for x in data if x < lower_bound or x > upper_bound]

# Plot chart with outliers
sns.boxplot(data=data)
sns.swarmplot(data=outliers, color='red', size=5, edgecolor='black')


#plt.hist(data, bins=30, alpha=0.5)

# Add median line
#plt.axvline(median, color='red', linestyle='dashed', linewidth=2)


# Add labels and title
plt.xlabel('Data')
plt.title('Chart with Mean, Min, Max, and Outliers')

# Show plot
plt.show()
