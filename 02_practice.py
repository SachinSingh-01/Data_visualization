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
# Legend'''
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
# a = np.random.randint(1, 50, 50)
# b = np.random.randint(1, 50, 50)
# plt.scatter(a, b, c='blue',s=50)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot")
# plt.show()

# Question 5
'''Create histogram of 1000 random numbers
✔ Customize:
bins
color
transparency'''
# random_no=np.random.randint(1,2000,(1000))
# plt.hist(random_no,bins=30,color="brown",alpha=0.5) #aplha use for transparency of the graph
# plt.show()
# print(random_no)

# Question 6
'''Create a bar chart:
students = ['A','B','C','D']
marks = [75, 85, 60, 90]
✔ Add:
title
labels'''
# students = ['A','B','C','D']
# marks = [75, 85, 60, 90]
# plt.bar(students,marks)
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Bar chart")
# plt.show()

# Question 7
'''Subplots
Create 2 plots side by side:
Left → line plot
Right → histogram'''
# a=[2,2,3]
# b=[3,3,5]
# fig,(ax1,ax2)=plt.subplots(1,2)
# ax1.plot(a,b)
# ax1.set_title("Line plot")
# ax2.hist(a)
# ax2.set_title("Hitogram")
# plt.show()

# Question 8
'''Plot a sine wave and:
✔ Mark maximum point using annotation'''
# a=np.linspace(2,4*np.pi,100)
# b=np.sin(a)
# plt.plot(a,b)
# idx=np.argmax(b)
# x_max=a[idx]
# y_max=b[idx]
# plt.annotate("|",(x_max,y_max))
# plt.show()

# Question 9
'''Create a plot and:
✔ Set custom x-ticks like: 0, 10, 20, 30
✔ Change labels (like "zero", "ten", etc.)'''
# x=[0,10,20,30]
# y = [10, 20, 30, 40] 
# plt.plot(x,y)
# plt.xticks([0,10,20,30])
# plt.xticks([0,10,20,30],["Zero","Ten","Twenty","Thirty"])
# plt.xlabel("X-axis")
# plt.ylabel("y-axis")
# plt.title("Custom Ticking")
# plt.show()

# Question 10
'''Dual Axis (twinx)
Plot:
Left axis → sine wave
Right axis → linear data'''
# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]
# b = np.sin(x)
# fig, ax1 = plt.subplots()
# ax1.plot(x, b, color='blue', label="Sine Wave")
# ax1.set_xlabel("X-axis")
# ax1.set_ylabel("Sine Wave", color='blue')
# ax2 = ax1.twinx()
# ax2.plot(x, y, color='red', label="Linear Data")
# ax2.set_ylabel("Linear Data", color='red')
# plt.title("Dual Axis Example")
# plt.show()

# Question 11
'''Create scatter plot:
✔ x, y random
✔ color based on third variable
# ✔ Add colorbar'''
# x=np.random.rand(50)
# y=np.random.rand(50)
# c=np.random.rand(50)
# plt.scatter(x,y,c=c)
# plt.scatter(x, y, c=c, cmap='viridis')
# plt.colorbar()
# plt.show()

# Question 12
'''Create plot where:
✔ y-axis is logarithmic'''
# x = [1,2,3,4,5]
# y = [10, 100, 1000, 10000, 100000]
# plt.plot(x,y)
# plt.yscale("log")
# plt.ylabel("Log scale")
# plt.show()

# Question 13
'''Create dataset:
students = ['A','B','C','D','E']
marks = [70, 85, 90, 60, 75]
study_hours = [2,4,5,1,3]
✔ Tasks:
Bar chart for marks
Scatter plot: study_hours vs marks
Add labels + title
Highlight highest scorer'''
# students = ['A','B','C','D','E']
# marks = [70, 85, 90, 60, 75]
# study_hours = [2,4,5,1,3]
# plt.bar(students,marks)
# plt.scatter(study_hours,marks,color="red",marker="*")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Mini project")
# idx=np.argmax(marks)
# plt.scatter(study_hours[idx], marks[idx], color='red', s=100)
# plt.show()

# Question 14
'''Create:
figure with yellow background
2 subplots
figure title
different axes titles'''
fig=plt.figure(facecolor="yellow")
plt.subplot(1,2,1)
plt.title("Left plot")
plt.plot([1,3,4],[6,7,5])

plt.subplot(1,2,2)
plt.title("Right plot")
plt.plot([7,8,9],[9,10,11])

plt.suptitle("axes")
plt.show()