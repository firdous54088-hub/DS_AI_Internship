# Task 1 Series creation and Indexing

import pandas as pd
products = pd.Series([700, 150, 300], index = ('Laptop', 'Mouse', 'Keyboard'))
print(products['Laptop'])
firsts2 = products[0:2]
print(firsts2)
print(products)

# Task 2 Boolean Masking and Missing Data

import pandas as pd
grades_values = pd.Series([85, None, 92, 45, None, 78, 55])
print(grades_values.isnull())
print(grades_values.fillna(0))
score = grades_values[grades_values>60]
print(score)
print(grades_values)

# Task 3 Vectorized string operations

import pandas as pd
usernames = pd.Series(['Alice', 'boB', 'Charlie_Data', 'daisy'])
low = usernames.str.lower()
print(low)
print(usernames.str.strip())
print(low.str.contains('a'))
