'''
Code for calculating root of a function.
The method used here is the Newton-Rapson.

Method:

f(x_0)=0

Taylor exp.

f(x_0) = f(x) + f'(x)(x_0-x)

- f(x)/f'(x) = x_0 - x

x_0 = x - f(x)/f'(x)

'''

import numpy as np
import math as math


def main():

	x_i_float = -15

	x_i_min_1_float = x_i_float+1e-5

	error_float = 1.0

	while( error_float > 1e-3 ):

		x_aux_float = x_i_float - function(x_i_float)/(analytical_derivative( x_i_float )+1e-8)
		error_float = math.fabs(x_aux_float - x_i_float)
		x_i_float = x_aux_float
		# print(analytical_derivative( x_i_float ))

	print( "Analytical procedure: ", np.around( x_i_float, 4) )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	x_i_float = 7.0

	x_i_min_1_float = x_i_float+1e-5

	error_float = 1.0

	while( error_float > 1e-3 ):

		x_aux_float = x_i_float - function( x_i_float )/(numerical_derivative( x_i_float, x_i_min_1_float )+1e-8)
		error_float = math.fabs(x_aux_float - x_i_float)
		x_i_min_1_float = x_i_float
		x_i_float = x_aux_float
		# print(error_float)
		# print( numerical_derivative( x_i_float, x_i_min_1_float ) )

	print( "Numerical procedure: ", np.around( x_i_float, 4) )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def function(x_float_):

	return(x_float_*x_float_-4.0)

def analytical_derivative( x_i_float_ ):
	
	return(2.0*x_i_float_)


def numerical_derivative( x_i_float_, x_i_min_1_float_ ):

	return(
		( function( x_i_float_ )-function( x_i_min_1_float_ ) )/( x_i_float_ - x_i_min_1_float_ + 1e-8)
	)

if __name__ == '__main__':
	main()