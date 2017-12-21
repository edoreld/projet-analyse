# This is a comment 

import matplotlib.pyplot as plt
import numpy as np

mean0 = [0, 0] # mu0
mean1 = [3, 2] # mu1
cov  = [[1, 0.5], [0.5, 1]] # cov

x1, y1 = np.random.multivariate_normal(mean0, cov, 1000).T # 
x2, y2 = np.random.multivariate_normal(mean1, cov, 1000).T

plt.plot(x1, y1, 'x', color="red")
plt.plot(x2, y2, "o", color="blue")
plt.axis('equal')
plt.show()
