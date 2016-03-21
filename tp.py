import numpy as np
from sklearn import metrics
from plot_ir import plot_ir
def evaluation(a,b,k):
	print(a)
	#a=[0,2,5,9,3,2,0]
	b=b.tolist()
	#print(b)
	#print(type(a))
	#print(type(b))
	#print("len a : %d"%len(a))
	#print("len b : %d"%len(b))
	b=b[:len(a)]
	
	#b=[1,3,4,9,3,2,1]
	#k=max(a)+1
	tp = [0.0]*k
	tn = [0.0]*k
	fp = [0.0]*k
	fn = [0.0]*k
	ran= [0.0]*k
	jac= [0.0]*k
	fm=[0*0]*k
	for i in range(0,len(a)):
		for j in range(0,len(a)):
			if a[i]==a[j] and i!=j and b[i]==b[j]:
				tp[a[i]] += 0.5
			
	#print tp
	for i in range(len(tp)):
		if tp[i]==0:
			tp[i]+=1
	for i in range(0,len(a)):
		for j in range(0,len(b)):
			if (a[i]!=a[j] and i!=j ) and b[i]!=b[j]:
				tn[a[i]] += 0.5
	for i in range(len(tn)):
		if tn[i]==0:
			tn[i]+=1
	#print tn

	for i in range(0,len(a)):
		for j in range(0,len(b)):
			if (a[i]!=a[j] and i!=j ) and b[i]==b[j]:
				fn[a[i]] += 0.5
	
	for i in range(len(fn)):
		if fn[i]==0:
			fn[i]+=1
	#print fn

	for i in range(0,len(a)):
		for j in range(0,len(b)):
			if (a[i]==a[j] and i!=j ) and b[i]!=b[j]:
				fp[a[i]] += 0.5
	
	for i in range(len(fp)):
		if fp[i]==0:
			fp[i]+=1
	#print fp

	
	'''
	for i in range(0,len(a)):
		for j in range(0,len(b)):
			if (a[i]==a[j] and i!=j ) and b[i]==b[j]:
				tp += 1
	'''
	for i in range(k):
		jac[i]=float(tp[i])/(tp[i]+fp[i]+fn[i])
		ran[i]=float(tp[i]+tn[i])/(tp[i]+fp[i]+fn[i]+tn[i])
		prec=float(tp[i])/(tp[i]+fp[i])
		rec=float(tp[i])/(tp[i]+fn[i])
		fm[i]=float(2*prec*rec)/(prec+rec)

	print("jac")
	print(jac)
	print("ran")

	print(ran)
	print("fm")
	print(fm)
	
	jac_tot=0
	ran_tot=0
	fm_tot=0
	tp_tot=0
	tn_tot=0
	fn_tot=0
	fp_tot=0
	for i in range(k):
		jac_tot+=jac[i]
		ran_tot+=ran[i]
		fm_tot+=fm[i]
		tp_tot+=tp[i]
		tn_tot+=tn[i]
		fn_tot+=fn[i]
		fp_tot+=tn[i]
	
	for i in range(k):
		jac_tot=float(tp_tot)/(tp_tot+fp_tot+fn_tot)
		ran_tot=float(tp_tot+tn_tot)/(tp_tot+fp_tot+fn_tot+tn_tot)
		prec=float(tp_tot)/(tp_tot+fp_tot)
		rec=float(tp_tot)/(tp_tot+fn_tot)
		fm_tot=float(2*prec*rec)/(prec+rec)


	#print("jac_tot")
	#print(jac_tot)
	#print("ran_tot")
	#print(ran_tot)
	#print("fm_tot")
	#print(fm_tot)
	
	tot=[0.0]*3
	tot[1]=jac_tot
	tot[0]=ran_tot
	tot[2]=fm_tot
	#print("new fm")
	#print(metrics.f1_score(a,b,average="macro"))
	#print("new jaccard")
	#print(metrics.jaccard_similarity_score(b, a))
	#print("new ran")
	#print(metrics.cluster.adjusted_rand_score(b,a))
	plot_ir(k,ran,jac,fm)
	'''
	def print_table(table):
	    col_width = [max(len(x) for x in col) for col in zip(*table)]
	    for line in table:
		print "| " + " | ".join("{:{}}".format(x, col_width[i])
		                        for i, x in enumerate(line)) + " |"

	table = [(str(x), str(f(x))) for x in mylist]
	print_table(table)
	'''
	print("Cluster no.     "),
	print("Rand        "),
	print("Jaccard     "),
	print("F-measure   ")
	for index in range(0,k):
		print (index+1),
		print  ("        "),
		print ("%.8f" %ran[index]),
		print  ("    "),
		print ("%.8f" %jac[index]),
		print  ("    "),
		print ("%.8f" %fm[index])
		
