''' 
Simple example for the interative interseption methods. It finds the
intersection points, just like the webcomb  method in non-linear dynamics.

It returns a point where the functions f and g have the same value. 
f(x_0) = g(x_0)

h(x_0) = f(x_0) - g(x_0) = 0

Taylor on h:

h(x_0) = h(x) + h'(x)*(x-x_0)

since h(x_0) = 0 

h(x) = - h'(x)*(x-x_0)

x_0 = x - h(x)/h'(x)

since h

h(x) = f(x) - g(x)

x_0 = x - [ f(x) - g(x) ] / [ f'(x) - g'(x) ]]
'''

import math as math
import numpy as np

def main():

	'''
	The test function are f(x) = 2*x-3 and g(x) = ln(x) 
	'''

	init_value_float =  0.1

	print( analytical_interseption(init_value_float) )

def analytical_interseption( x_i_float_ ):

	error_float = 1.0

	while( error_float > 1e-5 ):
		
		x_aux_float = x_i_float_ - (2.0*x_i_float_-3.0 - math.log(x_i_float_))/(2.0-1.0/x_i_float_)
		error_float = math.sqrt((x_i_float_ - x_aux_float)**2)
		x_i_float_ = x_aux_float

	return(x_i_float_)

if __name__ == '__main__':
	main()