# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:40:10 2026

@author: Raj Mohammad
"""

# Task 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew , kurtosis

df = pd.read_csv("housing.csv")
print(df.head())

plt.figure()
sns.histplot(df["price"],kde=True)
plt.title("Price Distribution")
plt.show()

# Calculate Skewness and kurtosis
price_skewness = skew(df["price"])
price_kurtosis = kurtosis(df["price"])

print("Skewness:",price_skewness)
print("Kurtosis:",price_kurtosis)

# for categorical data

plt.figure()
sns.countplot(x="airconditioning",data=df)
plt.title("Air conditioning")
plt.show()

# Task 2
# Scatter plot area vs price
plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(x="area",y="price",data=df)
plt.title("Area vs Price")
plt.show()

# Box Plot
plt.subplot(1,2,2)
sns.boxplot(x="parking",y="prefarea",data=df)
plt.title("Parking vs Prefarea")
plt.show()

print("\nScatter Plot Observation:")
print("As area increases, price seems to increase.")

print("\nBox Plot Observation:")
print("As parking increases, prefarea seems to increase.")

# Task 3

# Select only numeric columns
numeric_df = df.select_dtypes(include=['int64','float64'])

# Generate correalation matrix
corr_matrix = numeric_df.corr()

# Plot Heatmap
plt.figure()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.show()

#Boxplot for Outliers
plt.figure()
sns.boxplot(y=df["price"])
plt.title("Boxplot of House Prices")
plt.show()

# Print correlation values
print(corr_matrix)

