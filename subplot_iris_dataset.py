import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris_dataset = load_iris()

x_data = iris_dataset.data

y_target = iris_dataset.target

plot_1_fig = plt.figure(figsize=(5, 5))

ax = plt.Axes(plot_1_fig, [0., 0., 1., 1.])
ax.set_axis_off()

plot_1_fig = plt.grid()

plot_1_fig = plt.subplot(4,4,1)
plot_1_fig = plt.plot(0,0)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.text(0,0, 'Sepal Length', size=8,rotation=45, horizontalalignment='center', verticalalignment='center')
plot_1_fig = plt.subplot(4,4,2)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,1], x_data[:,0],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,3)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,2], x_data[:,0],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,4)
plot_1_fig = plt.xticks(np.arange(min(x_data[:,3]),max(x_data[:,3]),0.75))
plot_1_fig = plt.yticks(np.arange(min(x_data[:,0]),max(x_data[:,0]),0.75))
plot_1_fig = plt.plot(x_data[:,3], x_data[:,0],"+",markersize=3,linewidth=0.1)

plot_1_fig = plt.subplot(4,4,5)
# plot_1_fig = plt.xticks(np.arange(min(x_data[:,0]),max(x_data[:,0]),0.75))
plot_1_fig = plt.yticks(np.arange(min(x_data[:,1]),max(x_data[:,1]),0.75))
plot_1_fig = plt.plot(x_data[:,0], x_data[:,1],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,6)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(0,0)
plot_1_fig = plt.text(0,0, 'Sepal Width', size=8, rotation=45, horizontalalignment='center', verticalalignment='center')
plot_1_fig = plt.subplot(4,4,7)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,2], x_data[:,1],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,8)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,3], x_data[:,1],"+",markersize=3,linewidth=0.1)

plot_1_fig = plt.subplot(4,4,9)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,0], x_data[:,2],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,10)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,1], x_data[:,2],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,11)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(0,0)
plot_1_fig = plt.text(0,0, 'Petal Length', size=8, rotation=45, horizontalalignment='center', verticalalignment='center')
plot_1_fig = plt.subplot(4,4,12)
# plot_1_fig = plt.xticks(np.arange(min(x_data[:,3]),max(x_data[:,3]),0.75))
plot_1_fig = plt.yticks(np.arange(min(x_data[:,2]),max(x_data[:,2]),0.75))
plot_1_fig = plt.plot(x_data[:,3], x_data[:,2],"+",markersize=3,linewidth=0.1)

plot_1_fig = plt.subplot(4,4,13)
plot_1_fig = plt.yticks(np.arange(min(x_data[:,3]),max(x_data[:,3]),0.75))
plot_1_fig = plt.xticks(np.arange(min(x_data[:,0]),max(x_data[:,0]),0.75))
plot_1_fig = plt.plot(x_data[:,0], x_data[:,3],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,14)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,1], x_data[:,3],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,15)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(x_data[:,2], x_data[:,3],"+",markersize=3,linewidth=0.1)
plot_1_fig = plt.subplot(4,4,16)
plot_1_fig = plt.xticks([])
plot_1_fig = plt.yticks([])
plot_1_fig = plt.plot(0,0)
plot_1_fig = plt.text(0,0, 'Petal Width', size=8, rotation=45, horizontalalignment='center', verticalalignment='center')

# plt.show(plot_1_fig)

plt.savefig("subplot_iris_dataset.png", dpi=300)

plt.close()