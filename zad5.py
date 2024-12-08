import numpy as np
import matplotlib.pyplot as plt

A = np.random.randint(0, 100, (5, 5))

print("matrix A:")
print(A, "\n")

max_val = A.max()
min_val = A.min()
print("The biggest element in matrix:", max_val)
print("the smallest element in matrix:", min_val, "\n")

max_in_rows = A.max(axis=1)
print("The largest elements in each row:", max_in_rows)

max_in_cols = A.max(axis=0)
print("The largest elements in each column:", max_in_cols, "\n")

sum_in_rows = A.sum(axis=1)
print("Sum of values in individual rows:", sum_in_rows)
