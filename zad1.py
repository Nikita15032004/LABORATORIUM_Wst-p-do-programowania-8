import numpy as np
import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothes', 'Food', 'Toys', 'Books']
sales = [150, 200, 300, 100, 50]
plt.bar(categories, sales, color='skyblue')

plt.xlabel('Categories List')
plt.ylabel('Sales quantity')
plt.title('Sales by category')

plt.show()

