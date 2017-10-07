# A script to get first layer of hierarchically clustered samples in the IGC.
# commandline arguments are only one of the following files: AGC.clsr, CGC.clstr, EGC.clstr, SPGC.clstr
# Refer to run_cluster_of_clusters.sh for usage

import sys

f = sys.argv[1]
o = open(f[:-6]+'cluster_of_clusters.txt','w')
c = 0

cluster_recruits = {} # dictionary where keys are cluster centroids and values are cluster members

for i in open(f):
	if i.startswith('>'):
		continue
	else:
		c += 1
		i = i.split('\t')[1].strip()
		if i.endswith('*'):
			x = i.strip(' *')
			cluster_recruits[x] = []
		else:
			cluster_recruits[x].append(i.split(' at ')[0])

for k,v in cluster_recruits.items():
	o.write(k+'\t'+'\t'.join(v)+'\n') 

o.close()

print f+'\t'+str(c)+'\n' # prints total number of ORFs processed
