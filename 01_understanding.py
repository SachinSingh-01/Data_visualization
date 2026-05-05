import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5,11)
y=x**2

plt.figure()
plt.plot(x,y)
plt.title("Basic plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
# plt.show()

plt.figure()
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Plot 1")

plt.subplot(2,2,2)
plt.plot(x,y*2)
plt.title("Plot 2")

plt.subplot(2,2,3)
plt.plot(x,y*3)
plt.title("Plot 3")

plt.show()

fig=plt.figure()
a=fig.add_axes([0.1,0.1,1,1])
a.plot(x,y)
a.set_title("Main plot")

b=fig.add_axes([0.3,0.4,0.3,0.3])
b.plot(x,y)
b.set_title("Small plot")

plt.show()

fig=plt.figure(figsize=(20,8),dpi=100)
axis1=fig.add_axes([0.1,0.1,.4,.8])
axis1.plot(x,y)
axis1.set_title("dpi")

axis2=fig.add_axes([0.3,0.4,.3,.3])
axis2.plot(x,y)
axis2.set_title("big_dpi")

plt.show()
