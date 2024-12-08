import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(0, 50, size=(5, 5))

print("matrix:")
print(matrix)
print()

bigger_than_20 = matrix > 20
count = np.sum(bigger_than_20)
print(f"Qunatity of elements greather than 20: {count}")

mean_value = np.mean(matrix)
print(f"mean value of the matrix: {mean_value:.2f}")

plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='viridis')
plt.colorbar(label='values')

for i in range(5):
    for j in range(5):
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='white')

plt.title('matrix')
plt.show()