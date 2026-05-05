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
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel("y-axis")
# plt.title("First graph")
# plt.show()

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
# x = [1,2,3,4]
# y1 = [1,4,9,16]
# y2 = [1,2,3,4]
# y3 = [2,3,5,7]
# plt.plot(x,y1,label="data1")
# plt.plot(x,y2,label="data2")
# plt.plot(x,y3,label="data3")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Second graph")
# plt.legend()
# plt.show()

# Question 3
'''Marker + Style
Plot a line with:
markers
dashed line
custom color'''
# x = [1,2,3,4]
# y1 = [1,4,9,16]
# y2 = [1,2,3,4]
# y3 = [2,3,5,7]
# plt.plot(x,y1, marker="^",linestyle="--",color="pink")
# plt.show()

# Question 4
'''Scatter Plot
Generate random data using NumPy and create scatter plot
✔ Add:
color
size variation'''
# a=np.random.randint(1,8,(2,3))
# b=np.random.randint(9,18,(2,3))
# plt.figure(figsize=(10,3))
# plt.plot(a,b,color="green")
# plt.show()

# Question 5
'''Create histogram of 1000 random numbers
✔ Customize:
bins
color
transparency'''
random_no=np.random.randint(1,2000,(1000))
plt.hist(random_no)
plt.show()
print(random_no)

# Question 6
'''Create a bar chart:
students = ['A','B','C','D']
marks = [75, 85, 60, 90]
✔ Add:
title
labels'''
students = ['A','B','C','D']
marks = [75, 85, 60, 90]
plt.plot(students,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar chart")
plt.show()