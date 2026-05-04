import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5,11)
x
y=(x==3)
plt.plot(x,y)
y
plt.title("Hello")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.show()

# fig=plt.figure()
# a=fig.add_axes([0.1,0.1,1,1])
# result=a.plot(x,y)
# print(result)

# plt.subplot(2,2,1)
# plt.subplot(2,2,3)
# plt.subplot(2,2,2)
# plt.subplot(2,2,4)
# plt.plot(x,y)
# fig=plt.figure()
# b-fig.add_axes([0,3,0.4,0.3,0.3])
# b.plot(x,y)