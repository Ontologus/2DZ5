import matplotlib.pyplot as plt
import numpy as np
 %matplotlib inline
X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)
plt.scatter(X, Y, marker='^', label='график 1', s=15, color='red', alpha=0.4)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend()
plt.show()