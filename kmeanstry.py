from sklearn.datasets import fetch_20newsgroups
#from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.pipeline import make_pipeline
#from sklearn.preprocessing import Normalizer
from sklearn import metrics
from tp import evaluation


from math import *
import logging
#from optparse import OptionParser
import sys
from time import time

import numpy as np

#def euclidean(a,b):
	#for i in range
corpus = fetch_20newsgroups(subset="all")
data_samples=corpus.data
labels=corpus.target
#print(labels)
print("\n\n\n\n")
#print(max(labels))
#print(len(labels))
tfidf_vectorizer=TfidfVectorizer(max_df=0.95,min_df=2,stop_words='english')
#tfidf_feature_names=tfidf_vectorizer.get_feature_names()
#print(tfidf_feature_names)
a= CountVectorizer(min_df=1)
b= a.fit_transform(corpus.filenames)
vectorizer = TfidfTransformer()
x = vectorizer.fit_transform(b)
#print(x.get_feature_names())
x = x.toarray()
#print (x)

#print(x.size)
#print(np.prod(x.shape))
#print(len(x))
#print(len(x.T))
k = input("Enter the value of k")
b=np.random.randint(18846,size=k)
c=x[b,:]
#print(c)
#print(b)
#print(b[1])
#print(type(b))
cluster = [0]*400
for loop in range(0,1):  
	for p in range(0,400):
		eu_dist = [100000] * 400
		for cen_row in range(0,len(b)):	
			eusqr=0
			
			for q in range(0,15457):
				eusqr+= (x[p,q]-x[b[cen_row],q])*(x[p,q]-x[b[cen_row],q])

			eu_dist[cen_row]=sqrt(eusqr)	
			#print(cen_row )
			#print( eu_dist[cen_row])
		
			#print("     ")
		#print("")	
		cluster[p] = eu_dist.index(min(eu_dist))
		#print(cluster[p])
		#print(min(eu_dist))
	print(cluster)
	for  clus in range(0,k):
		count=0
		addindex= 0
		print ("")
		print("cluster" + repr(clus+1)),
		for inde in range (0,len(cluster)):
		
		
			if (cluster[inde]==clus):
				print(inde),
				#print("asd")	
				count+=1
				#print(count)	
				addindex += inde
		if (count !=0):	
			new_clus = floor(addindex/count)
		else:
			new_clus = np.random.randint(100)
		b[clus] = new_clus
	
	print(b)

print(cluster)


#print("Adjusted rand index : %f"%evaluation(labels,cluster,1))
#print("Jaccard: %f"%evaluation(labels,cluster,2))
#print("F-measure: %f"%evaluation(labels,cluster,0))

evaluation(cluster,labels,k)
	
					

	
