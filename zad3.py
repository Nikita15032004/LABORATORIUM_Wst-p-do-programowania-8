import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 10, 50)
speed = 10 * np.sin(time) + 20

plt.scatter(time, speed, color='blue', label='Instantaneous speed')

plt.xlabel('Time (s)')
plt.ylabel('Instantaneous Speed (km/h)')
plt.title('Instantaneous Speed of the Vehicle Over Time')

plt.legend()
plt.show()

#НИМАТЕЛЬНО ПРОВЕРИТЬ ПРАВИЛЬНОСТЬ ЭТОГО ЗАДАНИЯ
