import numpy as np
import matplotlib.pyplot as plt

def show_table(arr, title):
    plt.imshow(arr, cmap='OrRd')
    plt.grid(True)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])

plt.figure(figsize=(15, 3))

#A)
a = np.zeros((3, 3))
a[2, :] = 1

#B)
b = np.zeros((3, 3))
b[1:, 1] = 1

#C)
c = np.zeros((3, 3))
c[1:, :] = 1

#D)
d = np.zeros((3, 3))
d[0, [0,2]] = 1
d[1, [0,2]] = 1

#E)
e = np.zeros((3, 3))
e[1:, 1:] = 1

variants = [a, b, c, d, e]
titles = ['A', 'B', 'C', 'D', 'E']

for i in range(5):
    plt.subplot(1, 5, i+1)
    show_table(variants[i], titles[i])

plt.tight_layout()
plt.show()