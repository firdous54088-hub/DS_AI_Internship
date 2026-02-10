# Day 8 
# Task 1

import numpy as np

# Step 1: Create a 5x3 array of random scores (5 students, 3 subjects)
scores = np.random.randint(50, 101, size=(5, 3))

# Step 2: Calculate the mean of each subject (column-wise mean)
subject_means = scores.mean(axis=0)

# Step 3: Subtract the mean from the original scores using broadcasting
centered_scores = scores - subject_means

print("Original Scores:")
print("\nSubject-wise Mean:")
print("\nCentered Scores (After Normalization):")

print(scores)
print(subject_means)
print(centered_scores)


# Task 2

arr = np.arange(24)
reshaped = arr.reshape(4,3,2)
print(reshaped)

transposed = reshaped.transpose(0,2,1)
print(transposed)
