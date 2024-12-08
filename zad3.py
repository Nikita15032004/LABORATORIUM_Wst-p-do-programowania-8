import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 20) 
speed = 2.5 * np.sin(time) + 5

plt.scatter(time, speed, color='blue', marker='o', label='Prędkość')
plt.title("Prędkość pojazdu w czasie")
plt.xlabel("Czas s")
plt.ylabel("Prędkość m/s")
plt.grid(True)
plt.legend()
plt.show()
