import numpy as np
import matplotlib.pyplot as plt

matrix = np.zeros((5, 5))

matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1

def switch_values(mat):
    return 1 - mat

print("Initial matrix:")
print(matrix)

plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.imshow(matrix, cmap='binary')
plt.title('initial matrix')
plt.colorbar()

new_matrix = switch_values(matrix)

print("\nchanged matrix:")
print(new_matrix)

plt.subplot(122)
plt.imshow(new_matrix, cmap='binary')
plt.title('changed matrix')
plt.colorbar()

plt.tight_layout()
plt.show()