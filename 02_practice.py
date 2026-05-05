import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question 1
'''Simple Line Plot
Create a line plot for:
x = [1,2,3,4,5]
y = [2,4,6,8,10]
✔ Add:
X label
Y label
Title'''
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title("First graph")
plt.show()

# Question 2
'''Multiple Lines
Plot 3 lines on same graph:
x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [1,2,3,4]
y3 = [2,3,5,7]
✔ Add:
Labels for each line
Legend'''
x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [1,2,3,4]
y3 = [2,3,5,7]
plt.plot(x,y1,label="data1")
plt.plot(x,y2,label="data2")
plt.plot(x,y3,label="data3")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Second graph")
plt.legend()
plt.show()

# Question 3
'''Marker + Style
Plot a line with:
markers
dashed line
custom color'''
x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [1,2,3,4]
y3 = [2,3,5,7]
plt.plot(x,y1, marker="^",linestyle="--")
plt.show()