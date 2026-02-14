# Task 2

import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.bar(['Electronics', 'Clothing', 'Home'],[300, 450, 200])
plt.title("Bar Chart")
plt.subplot(1, 2, 2)
plt.plot([1,2,3],[4,5,6])
plt.title("Line Plot")
plt.tight_layout() 
plt.show()
