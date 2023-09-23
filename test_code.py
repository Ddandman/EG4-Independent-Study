import random
import numpy as np
import matplotlib.pyplot as plt

a_vec = []
for i in range(100000):
    a = np.random.normal(loc=3.0, scale=5.0, size=None)
    a_vec.append(a)

plt.hist(a_vec, 50)
plt.show()