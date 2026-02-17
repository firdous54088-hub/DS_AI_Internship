# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:14:45 2026

@author: Raj Mohammad
"""

# Task 1

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data ={
       "Transmission" : ["Autometic","manual","Autometic","manual"],
       "Color" : ["Red","Blue","Green","Red"],
      }


df = pd.DataFrame(data)
print(df)

# Apply label encoding to transmission
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])
print("\n After label encoding (Transmission):")
print(df)

# One-Hot Encoding 
df = pd.get_dummies(df, columns=["Color"], drop_first=True)
print("\n After One-Hot encoding (Color):")
print(df)


# Task 2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample data
data = {
    'Age': [20, 25, 30, 35, 40],
    'Salary': [20000, 30000, 40000, 50000, 60000]
}
df = pd.DataFrame(data)

# -----------------------------
# Standardization
# -----------------------------
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)

# -----------------------------
# Normalization
# -----------------------------
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)

# -----------------------------
# Histogram BEFORE scaling
# -----------------------------
plt.figure()
plt.subplot(1,3,1)
plt.hist(df['Salary'])
plt.title("Before Scaling (Salary)")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Histogram AFTER Standardization
# -----------------------------
plt.subplot(1,3,2)
plt.hist(df_standardized['Salary'])
plt.title("After Standardization (Salary)")
plt.xlabel("Scaled Salary")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Histogram AFTER Normalization
# -----------------------------
plt.subplot(1,3,3)
plt.hist(df_normalized['Salary'])
plt.title("After Normalization (Salary)")
plt.xlabel("Scaled Salary (0-1)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Task 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# -----------------------------
# Step 1: Create synthetic non-linear dataset
# -----------------------------
np.random.seed(42)

# X = Age, y = Salary has a quadratic relationship
X = np.array([22, 25, 30, 35, 40, 28, 50, 48, 33, 26]).reshape(-1,1)
y = np.array([25000, 30000, 50000, 70000, 90000, 45000, 120000, 110000, 60000, 35000])

# -----------------------------
# Step 2: Linear Regression on original feature
# -----------------------------
lin_model = LinearRegression()
lin_model.fit(X, y)
y_pred_linear = lin_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)
print(f"R² with original feature: {r2_linear:.4f}")

# -----------------------------
# Step 3: Polynomial Features (degree=2)
# -----------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)  # Creates [Age, Age^2]

# Optional: visualize features
print("Polynomial features (first 5 rows):")
print(X_poly[:5])

# -----------------------------
# Step 4: Linear Regression on polynomial features
# -----------------------------
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)
print(f"R² with polynomial features: {r2_poly:.4f}")

# -----------------------------
# Step 5: Visual Comparison
# -----------------------------
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, y_pred_linear, color='red', label='Linear Regression')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Regression (degree=2)')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()