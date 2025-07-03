import statistics as stats
import numpy as np

# Sample data
data = [12, 15, 14, 10, 18, 20, 22, 13, 17, 16]

# Mean
mean = stats.mean(data)

# Median
median = stats.median(data)

# Standard Deviation (sample)
std_dev = stats.stdev(data)

# Interquartile Range (IQR)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Display results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
print(f"IQR (Interquartile Range): {iqr}")

