'''
Simple example for logistic regression applied to the iris dataset.
Do not confuse with the logistic equation nor the replicator dynamics 
that uses the logistic equation, and neither the chaotic logsitic map.

Logistic regression is based of the Fermi-Dirac distribution for 
discrete classification or ocupation rate of fermions.


f(x;a,b;k) = b/(e**(-a*x)*k+1)

f(x) - the distribution (S shape)
a - scale parameter
b - linear parameter
x - canonical parameter
k - noise
'''

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_iris

def main():

	iris_dataset = load_iris()

	x_data = iris_dataset.data

	y_target = iris_dataset.target

	x_new_data = [[1,2,3,4],[5,6,7,8]] 

	logistic_reg_obj = LogisticRegression(
		solver="liblinear",
		multi_class="auto"
		)

	logistic_reg_obj.fit( x_data, y_target)

	print( logistic_reg_obj.predict(x_new_data) )


if __name__ == '__main__':
	main()