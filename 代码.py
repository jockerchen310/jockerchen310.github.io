import numpy as np
import matplotlib.pyplot as plt

plt.subplot(221)
t = np.linspace(-5.0,5.0,1000) 
plt.ylim(0,2)
x = np.exp(-1.5*t)
plt.plot(t,x)
x = np.exp(1.5*t)
plt.plot(t,x)
x = np.exp(0*t)
plt.plot(t,x)
plt.xlabel("t")
plt.ylabel("x")

plt.subplot(222)
x=np.arange(-2*np.pi,2*np.pi,0.01)
y=np.cos(x+1)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)

plt.subplot(223)
t=np.arange(-10,20,0.01)
x=0.2*np.exp(0.2*t)*np.cos(np.pi*t+0.5*np.pi)
plt.xlabel("t")
plt.ylabel("x")
plt.plot(t,x)

plt.subplot(224)
t=np.arange(-10,20,0.01)
x=0.2*np.exp(-0.2*t)*np.cos(np.pi*t+0.5*np.pi)
plt.xlabel("t")
plt.ylabel("x")
plt.plot(t,x)

plt.show()