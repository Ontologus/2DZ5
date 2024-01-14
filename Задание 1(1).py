import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
def y(x):
  return np.arctan(2 - 11 * x + x ** 2)
x = np.linspace(-10, 10, 500)
y = y(x)
plt.plot(x, y, color='g', dashes=[8, 4], label='Вот такая моя функция', alpha=0.5)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('y = arctg(2 - 11x + x**2)')
plt.legend()
plt.show()