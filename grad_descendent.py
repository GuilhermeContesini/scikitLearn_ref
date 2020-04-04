'''
Gradient Descendent method for calculating the local minimum(maximum) of a function.


Given f(x) we look for the point x_0 that minimizes(maximazes) the function.
We know that at minimum(mazimum) f'(x_0) = 0, therefore

Taylor expansion

f(x) = f(x_0) + f'(x_0)(x-x_0) + f''(x_0)*(x-x_0)**2

since f'(x_0) = 0

f(x) - f(x_0)  =  (1/2)*f''(x_0)*(x-x_0)*(x-x_0)

[f(x) - f(x_0)]/(x-x_0)  = (1/2)*f''(x_0)*(x-x_0)

again,
[f(x) - f(x_0)]/(x-x_0) = f'(x)

x_0 = x - 2*f'(x)/f''(x_0)

renaming x/f''(x_0) as alpha

if( f''(x_0)>0): x_0 is min and sign(f''(x_0)) = +1

elif( f''(x_0)>0 ): x_0 is max and sign(f''(x_0)>0) = -1


else: x_0 is a saddle point and the grad desc cannot be used.

x_0 = x - alpha * f'(x)

Note that alpha can be independent from the value of f''(x_0), but the sign must
be checked.

hints:

scale your data to the same range eg. a_1 = 5 b_1= 1000 c_1= 0.002 -> a_1
= 5 b_1= 1 * 1e3 c_1= 2 *1e-2

check if f(x_i) - f(x_i-1) < error to avoid flanten minima(maxima), such as
exp(x), 1/x, log(x).

alpha should be smaller than 1, or else the convergence is not asserted. However
a alpha too small returns a slow convergence. 1e-1, 1e-3, 1e-5 & 1e-8 

'''

def main():
	'''
	test function f(x) = x*x
	'''

	x_float = 10.0

	par_alpha_float = 0.5

	error_float = 1

	while(error_float > 1e-4 ):

		x_aux_float = x_float - par_alpha_float * der_function(x_float)
		error_float = x_aux_float - x_float
		x_float = x_aux_float

	print("minimum at:",x_float)

def der_function(x_float_):

	return(2*x_float_+1)



if __name__ == '__main__':
	main()