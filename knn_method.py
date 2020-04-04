import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

from sklearn.neighbors import KNeighborsClassifier


def main():

	iris_dataset = load_iris()

	x_data = iris_dataset.data

	y_features = iris_dataset.target

	x_new_data = [[1,2,3,4],[5,6,7,8]] 

	knn_obj = KNeighborsClassifier(
		n_neighbors=5,
		algorithm="ball_tree"
		)

	knn_obj.fit( x_data, y_features )

	print(knn_obj.predict(x_new_data))

if __name__ == '__main__':
	main()