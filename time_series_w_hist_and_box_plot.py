import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris_dataset = load_iris()

x_data = iris_dataset.data

y_target = iris_dataset.target

# ----------------------------------------------------------------------------------

left = 0.1
bottom = 0.1
width = 0.60
height = 0.65
spacing = 0.015
hist_width = 0.05


rect_scatter = [left, bottom, width, height]
rect_histx0 = [left + width + spacing, bottom, hist_width, height]
rect_histx1 = [left + width + (1*hist_width) + (2*spacing), bottom, hist_width, height]
rect_histx2 = [left + width + (2*hist_width) + (3*spacing), bottom, hist_width, height]
rect_histx3 = [left + width + (3*hist_width) + (4*spacing), bottom, hist_width, height]

plt.figure(figsize=(16, 9))

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction='in', top=True, right=True)

ax_histx0 = plt.axes(rect_histx0)
ax_histx0.tick_params(direction='in' , labelbottom=True)

ax_histx1 = plt.axes(rect_histx1)
ax_histx1.tick_params(direction='in' , labelbottom=True)

ax_histx2 = plt.axes(rect_histx2)
ax_histx2.tick_params(direction='in' , labelbottom=True)

ax_histx3 = plt.axes(rect_histx3)
ax_histx3.tick_params(direction='in' , labelbottom=True)

ax_scatter.set_ylim((0, max(x_data[:,0])+1))
ax_scatter.set_xlim(0, 150)

binwidth = 1
bins = np.arange(0, max(x_data[:,0]) + binwidth, binwidth)

ax_histx0.hist( x_data[ :, 0], bins = bins, color = "C0" , orientation = 'horizontal')
ax_histx1.hist( x_data[ :, 1], bins = bins, color = "C1" , orientation = 'horizontal')
ax_histx2.hist( x_data[ :, 2], bins = bins, color = "C2" , orientation = 'horizontal')
ax_histx3.hist( x_data[ :, 3], bins = bins, color = "C3" , orientation = 'horizontal')

# ----------------------------------------------------------------------------------

ax_scatter.plot( np.arange( 0, 150), x_data[ :, 0], "+", color = "C0", markersize =3, linewidth = 0.1)
ax_scatter.plot( np.arange( 0, 150), x_data[ :, 1], "d", color = "C1", markersize =3, linewidth = 0.1)
ax_scatter.plot( np.arange( 0, 150), x_data[ :, 2], "o", color = "C2", markersize =3, linewidth = 0.1)
ax_scatter.plot( np.arange( 0, 150), x_data[ :, 3], "^", color = "C3", markersize =3, linewidth = 0.1)
ax_scatter.legend(["sepal length ","sepal width","petal length","petal width"])

# plt.xticks(np.arange(0,160,10))

# plt.xlabel("# observation")
# plt.ylabel("feature")
# plt.grid()
# plt.show()

plt.savefig("scatterplot_iris_dataset.pdf")

plt.close()
