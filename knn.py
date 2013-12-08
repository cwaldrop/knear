'''
This script implements the k-nearest neighbors algorithm to classify inputs based
on a set of random training data.  This is mostly for practice, and the classifier
should not be expected to do well on purely random data.  Further enhancements could
include random data that drawn from two different distributions.  This would be more
illustrative of the effectiveness of knn. 
'''

import random
import sys
import matplotlib.pyplot as plt

def create_Data(nobs, datatype='Non-clustered'):
	'''
	Creates a list of tuples representing the x,y coordinates of training examples.  if
	the datatype argument is set to Non-clustered the datapoints will all come from
	the same distribution.  If datatype=Clustered then half of the datapoints will come from
	a N(0,1) and the other half will be drawn from a N(3,1) distribution.

	Parameters
	----------
	datatype: Determines the way in which datapoints are drawn.
	nobs: Number of observations.  How many data points are desired. 
	'''
	if datatype == 'Non-clustered':
		data = []
		for i in range(nobs):
			data.append((random.gauss(0,1), random.gauss(0,1)))
		return data

	elif datatype == 'Clustered':
		data = []
		for i in range(nobs/2):
			data.append((random.gauss(0,1), random.gauss(0,1)))
		for i in range(nobs/2):
			data.append((random.gauss(3,1), random.gauss(3,1)))
		return data

def plot_Data(data):
	'''
	Takes a list of datapoints and graphs them in a scatterplot. 
	'''
	print data

	for i in range(len(data)):
		x, y = data[i-1]
		plt.scatter(x,y)


if __name__ == '__main__':
	nobs = int(sys.argv[1])

	data = create_Data(nobs)
	plot_Data(data)
	plt.show()





