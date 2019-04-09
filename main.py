import numpy as np #Imports Python mathematical functions library
import matplotlib.pyplot as plt #Imports plot library
cos = np.cos
pi = np.pi

a = 5
e = 0.99
theta = np.linspace(0,2*pi, 360)
r = (a*(1-e**2))/(1+e*cos(theta))
plt.polar(theta, r)

print(np.c_[r,theta])

plt.show()