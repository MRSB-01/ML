import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = np.random.normal(size=1000)

plt.hist(data,bins=100, density=True, alpha=0.7, color="blue", label="histogram")

x = np.linspace(-3,3,1000)

plt.plot(x,norm.pdf(x), color="yellow", linewidth=2, label="Normal Distribution")
plt.xlabel("value")
plt.ylabel("den")
plt.title("Normal  Distributio of random data ")
plt.legend()
plt.show()
