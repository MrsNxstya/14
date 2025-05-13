import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 7, 1000)

y = 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)

plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$Y(x)=\frac{5 \cdot \sin(10x) \cdot \sin(3x)}{\sqrt{x}}$')

plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x)')
plt.legend()
plt.grid(True)

plt.show()
