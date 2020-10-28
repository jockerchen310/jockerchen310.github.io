import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10.0,10.0,1000) 
plt.ylim(0,5)

ft = np.exp(-1.5*t)
plt.plot(t,ft)

ft1 = np.exp(1.5*t)
plt.plot(t,ft1)

ft2 = np.exp(0*t)
plt.plot(t,ft2)

plt.xlabel("t")
plt.ylabel("x")
plt.show()