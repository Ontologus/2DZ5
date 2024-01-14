import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
data = np.random.normal(16, 2, 1000)
plt.hist(data, bins=15, color='red', alpha=0.5)
plt.show()
#в основном бегут за 16 секунд