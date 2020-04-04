'''
linear regression example for breast cancer dataset using sklearn mod.

'''
import numpy as np
import math as math
import pandas as pd 

import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

which = lambda value_list:list( np.where( value_list == 'None' )[0] )

def main():

	data_csv_file = pd.read_csv( "auto-mpg.csv" )

	x_feature_data = data_csv_file.iloc[ :, 3 ]

	x_drop_values_list = which( x_feature_data )

	proc_data = data_csv_file.drop( x_drop_values_list )

	length_proc_data = proc_data.shape[0]

	x_feature_data = proc_data.iloc[ :, 3 ]

	y_target_data = proc_data.iloc[ :, 0 ]

	x_feature_data = x_feature_data[ :, np.newaxis ]

	x_train_data = x_feature_data[ int( -1*length_proc_data/2 ): ]
	x_test_data = x_feature_data[ :int( -1*length_proc_data/2 ) ]

	y_train_target = y_target_data[ int( -1*length_proc_data/2 ): ]
	y_test_target = y_target_data[ :int( -1*length_proc_data/2 ) ]

	regr_model_obj = linear_model.LinearRegression()

	regr_model_obj.fit( x_train_data, y_train_target )	

	y_predicted_target = regr_model_obj.predict( x_test_data )

	print(
		"Coefficients:",
		regr_model_obj.coef_
	)

	print(
		'Mean squared error:'
		% mean_squared_error( y_test_target, y_predicted_target )
	)

	print(
		'R2: %.2f'
		% r2_score( y_test_target, y_predicted_target )
	)

	# plt.plot(
 #        x_test_data,
 #        y_test_target,
 #        '+',
 #        markersize=3,
 #        color='red',
 #        linewidth=0.1
 #    )
	
	# plt.plot(
	# 	x_test_data,
	# 	y_predicted_target,
	# 	color='blue',
	# 	linewidth=0.75
	# )

	# plt.xticks(())
	# plt.yticks(())

	plt.show()


if __name__ == '__main__':
	main()