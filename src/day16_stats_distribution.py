# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:16:09 2026

@author: Raj Mohammad
"""
# Task 1
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate Datasets

# Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=5, size=500)

# Right-Skewed Distribution (Household Income)
income = np.random.lognormal(mean=10, sigma=0.5, size=500)

# Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.lognormal(mean=3, sigma=0.4, size=500)

# Convert to Pandas Series
heights = pd.Series(heights)
income = pd.Series(income)
scores = pd.Series(scores)


# 2. Function to Plot & Compare

def analyze_data(data, title):
    mean = data.mean()
    median = data.median()
    
    print(f"\n{title}")
    print("Mean   :", round(mean, 2))
    print("Median :", round(median, 2))
    
    if mean > median:
        print("Observation: Right-Skewed Distribution")
    elif mean < median:
        print("Observation: Left-Skewed Distribution")
    else:
        print("Observation: Normal Distribution")
    
    # Plot
    plt.figure(figsize=(6,4))
    sns.histplot(data, kde=True)
    plt.axvline(mean, color='red', linestyle='--', label='Mean')
    plt.axvline(median, color='green', linestyle='-', label='Median')
    plt.title(title)
    plt.legend()
    plt.show()

# 3. Analyze All Datasets

analyze_data(heights, "Human Heights (Normal Distribution)")
analyze_data(income, "Household Income (Right-Skewed)")
analyze_data(scores, "Easy Exam Scores (Left-Skewed)")

# Task 2

import numpy as np
import pandas as pd

np.random.seed(42)

# 1. Generate Dataset (Heights Example)

# Normal dataset
data = np.random.normal(loc=170, scale=5, size=100)

# Add extreme outliers manually
data = np.append(data, [200, 210, 130])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Height"])

# 2. Calculate Mean and Std Dev

mu = df["Height"].mean()
sigma = df["Height"].std()

print("Mean (μ):", round(mu, 2))
print("Standard Deviation (σ):", round(sigma, 2))

# 3. Calculate Z-Score

df["z_score"] = (df["Height"] - mu) / sigma

# 4. Identify Outliers (|Z| > 3)

outliers = df[np.abs(df["z_score"]) > 3]


print("\nOutliers Detected:")
print(outliers)
print("\nTotal Outliers:", len(outliers))
# Task 3

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.exponential(scale=50000, size=100000)

df = pd.DataFrame({"Income": population})

# plot histogram for skewed data
plt.figure(figsize=(6,4))
sns.histplot(df["Income"], bins=50, kde=True)
plt.title("Original Population Distribution (Right-Skewed)")
plt.show()

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())

sample_means = pd.Series(sample_means)

# plot histogram for sample distrubution
plt.figure(figsize=(6,4))
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.show()