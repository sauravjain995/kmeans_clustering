import numpy as np
import matplotlib.pyplot as plt
def plot_ir(k,ran,jac,fm):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	## the data
	N = k
	menMeans = ran
	menStd =   [0]*k
	womenMeans = jac
	womenStd =   [0]*k
	chMeans = fm
	#ch1Means = tot
	## necessary variables
	ind = np.arange(N)                # the x locations for the groups
	width = 0.1                      # the width of the bars

	## the bars
	rects1 = ax.bar(ind, menMeans, width,
					color='black',
					yerr=menStd,
					error_kw=dict(elinewidth=2,ecolor='red'))

	rects2 = ax.bar(ind+width, womenMeans, width,
						color='red',
						yerr=womenStd,
						error_kw=dict(elinewidth=2,ecolor='black'))
						
	rects3 = ax.bar(ind+2*width, chMeans, width,
					color='green',
					yerr=menStd,
					error_kw=dict(elinewidth=2,ecolor='green'))

	#rects4 = ax.bar(ind+3*width, ch1Means, width,
	#				color='orange',
	#				yerr=menStd,
	#				error_kw=dict(elinewidth=2,ecolor='blue'))
	#

	# axes and labels
	ax.set_xlim(-width,len(ind)+width)
	ax.set_ylim(0,2)
	ax.set_ylabel('Values')
	ax.set_title('Clusterwise Rand Jaccard and F-measure')
	xTickMarks = ['Cluster'+str(i) for i in range(1,k+1)]
	ax.set_xticks(ind+width)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=45, fontsize=10)

	## add a legend
	ax.legend( (rects1[0], rects2[0],rects3[0]), ('ran', 'jac','fm') )

	plt.show()

