import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,3,5,7,11])
z = np.polyfit(x,y,1)
p = np.poly1d(z)

plt.scatter(x,y)
plt.plot(x, p(x), "r--")
plt.show()