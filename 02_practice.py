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
# fig=plt.figure(facecolor="yellow")
# plt.subplot(1,2,1)  # here 1 for rows, 2 for column, 1 for position (leftmost)
# plt.title("Left plot")
# plt.plot([1,3,4],[6,7,5])

# plt.subplot(1,2,2) # here 1 for rows, 2 for column, 2 for position (rightmost)
# plt.title("Right plot")
# plt.plot([7,8,9],[9,10,11])

# plt.suptitle("axes")
# plt.show()

# Question 15
'''Understand Figure vs Axes
Create:
one Figure
one Axes
Requirements:
figure background color
figure title
axes title
custom figure size'''
# fig=plt.figure(figsize=(2,4),
#                   layout="constrained",
#                   facecolor="yellow")
# fig.suptitle("Sachin",fontsize=20)
# ax=fig.add_subplot()
# ax.set_title("Figure")
# plt.plot([2,3,4],[5,6,7])
# plt.show()

# Question 16
'''Create:
2 rows x 2 columns
Requirements:
each subplot must have different title
different background colors
different line plots'''
# plt.subplot(2,2,1,facecolor="pink")
# plt.title("Fig-1")
# plt.plot([3,4,5],[6,7,8])

# plt.subplot(2,2,2,facecolor="yellow" )
# plt.title("Fig-2")
# plt.plot([10,12,14],[6,7,8])

# plt.subplot(2,2,3,facecolor="brown" )
# plt.title("Fig-3")
# plt.plot([6,7,9],[9,7,3])

# plt.subplot(2,2,4,facecolor="gold" )
# plt.title("Fig-4")
# plt.plot([11,13,15],[9,7,3])

# plt.show()

# Question 17
'''Create a figure with:
4 subplots
Add:
figure-wide x-label
figure-wide y-label
figure-wide title'''
# fig=plt.figure(figsize=(8,6))
# plt.subplot(2,2,1)
# plt.plot([1,2,3],[4,5,6])
# plt.title("Fig-1")

# plt.subplot(2,2,2)
# plt.plot([7,4,6],[8,4,3])
# plt.title("Fig-2")

# plt.subplot(2,2,3)
# plt.plot([4,2,6],[9,8,5])
# plt.title("Fig-3")

# plt.subplot(2,2,4)
# plt.plot([4,2,3],[8,1,3])
# plt.title("Fig-4")

# fig.text(0.5, 0.04, "X-axis", ha='center')
# fig.text(0.04, 0.5, "Y-axis", va='center', rotation='vertical')
# plt.tight_layout()
# plt.show()

# Question 18
'''Create:
4 crowded subplots
long titles
long labels
First:
❌ without constrained layout
Then:
✅ with constrained layout'''
# plt.figure(figsize=(8,6))
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")

# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.show()

# plt.figure(figsize=(8,6),constrained_layout=True)
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.show()

# Question 19
'''Create same figure using:
constrained
tight
compressed
Analyze:
spacing
alignment
readability'''
# plt.figure(figsize=(8,6),layout="tight")
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")


# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.show()


# plt.figure(figsize=(8,6),layout="compressed")
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")


# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.show()

# plt.figure(figsize=(8,6),layout="constrained")
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")


# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")

# plt.show()

# Question 20
'''Save same figure with:
dpi=50
dpi=100
dpi=300
Compare:
quality
sharpness
file size'''
# plt.figure(figsize=(8,6))
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")


# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")
# plt.savefig("figdpi-50.png",dpi=50)

# plt.show()


# plt.figure(figsize=(8,6))
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")


# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")
# plt.savefig("figdpi-100.png",dpi=100)

# plt.show()

# plt.figure(figsize=(8,6))
# plt.subplot(2,2,1)
# plt.plot([4,5,6],[7,8,9])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-1")


# plt.subplot(2,2,2)
# plt.plot([8,6,9],[3,7,4])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-2")

# plt.subplot(2,2,3)
# plt.plot([8,3,7],[9,3,5])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-3")

# plt.subplot(2,2,4)
# plt.plot([7,3,2],[8,1,2])
# plt.xlabel("This is a very long x-axis label")
# plt.ylabel("This is a very long y-axis label")
# plt.title("This is a very long subplot title example-4")
# plt.savefig("figdpi-300.png",dpi=300)

# plt.show()

# Question 21
'''Create:
dashboard-style figure
Requirements:
1 large plot on top
2 small plots below
figure title
custom colors
Hint:use:subplot_mosaic()'''
# fig,ax=plt.subplot_mosaic(
#     [
#         ["top","top"],
#         ["left","right"]
#     ],
#     figsize=(8,6)
# )
# ax["top"].plot([3,4,7,2],[2,6,8,6],color="blue")
# ax["top"].set_title("Top plot")
# ax["top"].set_facecolor("yellow")

# ax["left"].plot([9,7,4,3],[4,8,9,3],color="red")
# ax["left"].set_title("left plot")
# ax["left"].set_facecolor("green")

# ax["right"].plot([2,5,7,8],[9,6,3,5],color="brown")
# ax["right"].set_title("right plot")
# ax["right"].set_facecolor("purple")
# plt.suptitle("Dashboard style figure",fontsize=20)
# plt.tight_layout()
# plt.show()

# Question 22
'''Create:
one main figure
left subfigure
right subfigure
Requirements:
left subfigure → 2 vertical plots
right subfigure → 2 horizontal plots
different subfigure colors'''
# fig = plt.figure(layout='constrained', facecolor='lightskyblue')

# figL,figR=fig.subfigures(1,2)
# axL=figL.subplots(2,1)
# axL[0].plot([6,7,2],[8,9,2])
# axL[0].set_title("Left plot")
# axL[1].plot([6,7,2],[8,9,2])
# axL[1].set_title("Left plot")
# figL.set_facecolor("green")

# axR=figR.subplots(1,2)
# axR[0].plot([4,7,9],[2,7,5])
# axR[0].set_title("Right plot")
# axR[1].plot([4,7,9],[2,7,5])
# axR[1].set_title("Right plot")
# figR.set_facecolor("pink")
# plt.show()

# Question 23
'''Create figure and save:
PNG
PDF
SVG
Compare:
zoom quality
file size
sharpness'''
# fig = plt.figure(layout='constrained', facecolor='lightskyblue')

# figL,figR=fig.subfigures(1,2)
# axL=figL.subplots(2,1)
# axL[0].plot([6,7,2],[8,9,2])
# axL[0].set_title("Left plot")
# axL[1].plot([6,7,2],[8,9,2])
# axL[1].set_title("Left plot")
# figL.set_facecolor("green")

# axR=figR.subplots(1,2)
# axR[0].plot([4,7,9],[2,7,5])
# axR[0].set_title("Right plot")
# axR[1].plot([4,7,9],[2,7,5])
# axR[1].set_title("Right plot")
# figR.set_facecolor("pink")
# plt.savefig("Myfig.png")
# plt.savefig("Myfig.pdf")
# plt.savefig("Myfig.svg")
# plt.show()

# Question 24
'''Save same figure:
normal
bbox_inches='tight'''
# fig = plt.figure(layout='constrained', facecolor='lightskyblue')

# figL,figR=fig.subfigures(1,2)
# axL=figL.subplots(2,1)
# axL[0].plot([6,7,2],[8,9,2])
# axL[0].set_title("Left plot")
# axL[1].plot([6,7,2],[8,9,2])
# axL[1].set_title("Left plot")
# figL.set_facecolor("green")

# axR=figR.subplots(1,2)
# axR[0].plot([4,7,9],[2,7,5])
# axR[0].set_title("Right plot")
# axR[1].plot([4,7,9],[2,7,5])
# axR[1].set_title("Right plot")
# figR.set_facecolor("pink")
# plt.savefig("normal.png")
# plt.savefig("right.png",bbox_inches="tight")
# plt.show()

# Question 25
'''Create ONE figure containing:
line plot
histogram
scatter plot
bar chart'''
# plt.figure(figsize=(8,6))
# plt.subplot(2,2,1)
# data=[3,4,7,8,9]
# plt.plot(data)
# plt.title("Line plot")

# plt.subplot(2,2,2)
# data1=[8,9,4,7,3]
# plt.hist(data1)
# plt.title("Histogram plot")

# plt.subplot(2,2,3)
# x=[9,7,4,8,9]
# y=data1
# plt.scatter(x,y)
# plt.title("Scatter plot")

# plt.subplot(2,2,4)
# x=[7,8,5,3,9]
# y=data
# plt.bar(x,y)
# plt.title("Bar plot")

# plt.tight_layout()
# plt.show()

# Question 26
'''Recreate a Real Dashboard
Search inspiration from:
finance dashboards
ML dashboards
analytics reports
Try recreating layout using:
subplot_mosaic
subfigures
custom figsize
constrained layout'''
# fig,ax=plt.subplot_mosaic(
#     [
#     ["top", "top"],
#     ["left", "right"],
#     ["bottom", "bottom"]
# ],
#     figsize=(8,6),
#     layout="constrained"
# )
# ax["top"].plot([5,7,8,9,6])
# ax["top"].set_title("Line plot")

# x=[7,8,6,5]
# y=[7,9,2,4]
# ax["left"].scatter(x,y)
# ax["left"].set_title("scatter plot")

# a=[7,9,2,7,5]
# ax["right"].hist(a)
# ax["right"].set_title("Histogram Plot")

# s=[8,9,5,3,2]
# k=[6,4,3,9,0]
# ax["bottom"].bar(s,k)
# ax["bottom"].set_title("Bar plot")

# plt.tight_layout()
# plt.show()

# Question 27
'''Create SAME graph using:
pyplot interface
explicit axes interface
Then compare:
readability
flexibility
scalability'''

# Using pyplot interface
# plt.figure(figsize=(8,2))
# plt.subplot(1,2,1)
# plt.plot([5,7,8],[3,2,1])
# plt.title("Pyplot interface 1")
# plt.subplot(1,2,2)
# plt.plot([3,2,7],[2,9,6])
# plt.title("Pyplot interface 2")

# # Using explicit  interface
# fig,ax=plt.subplots(1,2)
# ax[0].plot([5,7,8],[3,2,1])
# ax[0].set_title("Explicit interface 1")
# ax[1].plot([3,2,7],[2,9,6])
# ax[1].set_title("Explicit interface 2")
# plt.show()

# Question 28
'''Create:
2 subplots using pyplot
modify first subplot after creating second subplot
Do:
using subplot() recall
using explicit axes
Observe difference.'''
# plt.figure(figsize=(8,2))
# plt.subplot(1,2,1)
# plt.plot([4,9,3],[5,3,2])
# plt.title("Figure 1")

# plt.subplot(1,2,2)
# plt.plot([8,3,1],[9,5,4])
# plt.title("Figure 2")

# plt.subplot(1,2,1)
# plt.title("Modified")

# fig,ax=plt.subplots(1,2)
# ax[0].plot([4,9,3],[5,3,2])
# ax[1].plot([8,3,1],[9,5,4])

# ax[0].set_title("Modified")
# plt.show()

# Question 29
'''Use:
plt.gca()
plt.gcf()
Print:
current axes
current figure
after different plotting operations.
Goal
Understand pyplot state machine deeply.'''
# plt.figure(figsize=(8,9))
# plt.subplot(1,2,1)
# plt.plot([56,45,34],[34,56,78])
# plt.title("Get currect figure/ Get current axis -1")
# print(plt.gca())
# print(plt.gcf())
# plt.subplot(1,2,2)
# plt.plot([67,87,54],[78,98,88])
# plt.title("Get currect figure/ Get current axis -2")
# print(plt.gca())
# print(plt.gcf())
# plt.show()

# Question 30
'''Create:
4 subplots using pyplot only
Then:
accidentally modify wrong subplot
debug issue
Goal
Experience pyplot confusion practically.'''
# plt.figure(figsize=(8,2))
# plt.subplot(2,2,1)
# plt.plot([56,76,45],[3,4,5])
# plt.title("First figure")

# plt.subplot(2,2,2)
# plt.plot([76,34,23],[6,9,2])
# plt.title("Second figure")

# plt.subplot(2,2,3)
# plt.plot([5,7,5],[67,34,21])
# plt.title("Third figure")

# plt.subplot(2,2,4)
# plt.plot([76,45,45],[23,45,12])
# plt.title("Fourth figure")

# # Modify
# plt.subplot(2,2,1)
# plt.title("Modified")

# plt.show()

# Question 31
'''Create dashboard:
4 subplots
legends
titles
annotations
ONLY using explicit axes style.
Goal
Build professional plotting habit.'''
# fig,ax=plt.subplots(2,2)
# ax[0,0].plot([4,5,7],[6,4,3],label="Data 1")
# ax[0,0].legend(loc="upper left")
# ax[0,0].annotate("Highest",(4,6))
# ax[0,0].set_title("Fig-1")

# ax[0,1].plot([7,5,3],[4,3,2],label="Data 2")
# ax[0,1].legend(loc="upper left")
# ax[0,1].annotate("Highest",(5,2))
# ax[0,1].set_title("Fig-2")

# ax[1,0].plot([6,7,4],[9,2,4],label="Data 3")
# ax[1,0].legend(loc="lower right")
# ax[1,0].annotate("Highest",(4,4))
# ax[1,0].set_title("Fig-3")

# ax[1,1].plot([3,2,6],[7,8,3],label="Data 4")
# ax[1,1].legend(loc="lower right")
# ax[1,1].annotate("Highest",(6,8))
# ax[1,1].set_title("Fig 4")
# plt.show()

# Question 32
'''Create helper function:
def my_plot(ax, x, y):
Pass different axes into function.'''
# def my_plot(ax, x, y):
#     ax.plot(x,y)
# x=[4,5,7,8]
# y=[4,3,2,6]
# a=[67,54,33,23]
# b=[34,23,64,23]
# fig,ax=plt.subplots(2,2)
# my_plot(ax[0,0],x,y)
# my_plot(ax[0,1],a,b)
# plt.show()

# Question 33
'''Create custom class:
class MyData:
Store:
x
y
Implement:
plot()
with optional:
ax=None
Goal
Understand how pandas/seaborn style APIs work internally.'''
# class MyData:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         plt.plot([3,4,5,3],[2,6,4,2])
#         plt.show()

# Question 34
'''Build mini analytics dashboard:
multiple axes
pass axes into helper functions
save figure
ONLY explicit interface allowed.
Goal
Simulate real project architecture.'''
# def my_plot(ax,x,y):
#     ax.plot(x,y,label="data")
# x=[6,4,3,2]
# y=[5,9,2,1]
# fig,ax=plt.subplots(2,2,figsize=(8,2))
# my_plot(ax[0,0],x,y)
# ax[0,0].set_title("First figure")
# ax[0,0].legend(loc="upper left")
# ax[0,0].annotate("Highest",(5,2))

# my_plot(ax[0,1],x,y)
# ax[0,1].set_title("Second figure")
# ax[0,1].legend(loc="upper right")
# ax[0,1].annotate("Highest",(4,3))

# my_plot(ax[1,0],x,y)
# ax[1,0].set_title("Third figure")
# ax[1,0].legend(loc="lower left")
# ax[1,0].annotate("Highest",(2,5))

# my_plot(ax[1,1],x,y)
# ax[1,1].set_title("Fourth figure")
# ax[1,1].legend(loc="lower right")
# ax[1,1].annotate("Highest",(3,3))
# plt.savefig("Mini_dataplot.png")
# plt.show()

# Question 35
'''Try creating:
6 subplot dashboard
First with pyplot only.
Then with explicit axes.
Compare:
debugging
readability
control
Goal
Feel WHY explicit interface wins.'''
plt.figure(figsize=(8,2))

plt.subplot(2,3,1)
plt.plot([56,76,45],[3,4,5])
plt.title("First figure")

plt.subplot(2,3,2)
plt.plot([76,34,23],[6,9,2])
plt.title("Second figure")

plt.subplot(2,3,3)
plt.plot([5,7,5],[67,34,21])
plt.title("Third figure")

plt.subplot(2,3,4)
plt.plot([76,45,45],[23,45,12])
plt.title("Fourth figure")

plt.subplot(2,3,5)
plt.plot([45,23,62],[23,4,1])
plt.title("Fifth figure")

plt.subplot(2,3,6)
plt.plot([54,2,12],[23,61,23])
plt.title("Sixth figure")
plt.show()

# Explicit function

fig,ax=plt.subplots(2,3)
ax[0,0].plot([4,5,7],[6,4,3],label="Data 1")
ax[0,0].legend(loc="upper left")
ax[0,0].annotate("Highest",(4,6))
ax[0,0].set_title("Fig-1")

ax[0,1].plot([7,5,3],[4,3,2],label="Data 2")
ax[0,1].legend(loc="upper left")
ax[0,1].annotate("Highest",(5,2))
ax[0,1].set_title("Fig-2")

ax[1,0].plot([6,7,4],[9,2,4],label="Data 3")
ax[1,0].legend(loc="lower right")
ax[1,0].annotate("Highest",(4,4))
ax[1,0].set_title("Fig-3")

ax[1,1].plot([3,2,6],[7,8,3],label="Data 4")
ax[1,1].legend(loc="lower right")
ax[1,1].annotate("Highest",(7,4))
ax[1,1].set_title("Fig 4")

ax[0,2].plot([7,2,8],[2,9,4],label="Data 5")
ax[0,2].legend(loc="lower right")
ax[0,2].annotate("Highest",(4,3))
ax[0,2].set_title("Fig 5")

ax[1,2].plot([5,8,3],[9,4,2],label="Data 6")
ax[1,2].legend(loc="lower right")
ax[1,2].annotate("Highest",(2,5))
ax[1,2].set_title("Fig 6")
plt.show()